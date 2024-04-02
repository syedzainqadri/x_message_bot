const express = require('express');
const admin = require('firebase-admin');
const { initializeApp } = require('firebase/app');
var firebaseConfig = {
    apiKey: "AIzaSyBmb0TAnTBB3dlzAg5EZmy_pf3tfGikbgE",
    authDomain: "monkeyslist-promoters.firebaseapp.com",
    projectId: "monkeyslist-promoters",
    storageBucket: "monkeyslist-promoters.appspot.com",
    messagingSenderId: "1077736306396",
    appId: "1:1077736306396:web:0331e814abc18fae28e619",
    measurementId: "G-VWXHY3J50F"
};
const initailized = initializeApp(firebaseConfig);
console.log("Firebase is connected successfully.");
const db = admin.firestore();
const auth = admin.auth();
const app = express();
const port = process.env.PORT || 3000; // Port from environment or default
app.use(express.json());
// Route to handle GET posts request
app.post('/api/getPosts', async (req, res) => {
  const { email, password } = req.body;

  try {
    // Authenticate user and get custom token
    const userRecord = await auth.getUserByEmail(email);
    const customToken = await auth.createCustomToken(userRecord.uid);

    // Query Firestore for user's posts
    const postsRef = db.collection('users').doc(userRecord.uid).collection('posts');
    const snapshot = await postsRef.get();

    if (snapshot.empty) {
      return res.status(404).json({ message: 'No posts found for this user.' });
    }

    let postsData = [];
    snapshot.forEach(doc => {
      postsData.push(doc.data());
    });

    return res.status(200).json({ token: customToken, posts: postsData });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).send('Internal Server Error');
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
  console.log('Firebase connected successfully'); // Log on server start
});
