const express = require('express');
const admin = require('firebase-admin');
const { initializeApp } = require('firebase/app');
const { getAuth, signInWithEmailAndPassword } = require('firebase/auth');
const { getFirestore, collection, query, where, getDocs } = require('firebase/firestore');
const fs = require('fs');
var firebaseConfig = {
    apiKey: "AIzaSyBmb0TAnTBB3dlzAg5EZmy_pf3tfGikbgE",
    authDomain: "monkeyslist-promoters.firebaseapp.com",
    projectId: "monkeyslist-promoters",
    storageBucket: "monkeyslist-promoters.appspot.com",
    messagingSenderId: "1077736306396",
    appId: "1:1077736306396:web:0331e814abc18fae28e619",
    measurementId: "G-VWXHY3J50F"
};
const firebaseApp = initializeApp(firebaseConfig);
const auth = getAuth();
const db = getFirestore();

const app = express();
app.use(express.json());

// Function to fetch user posts
async function fetchUserPosts(userId) {
    const postsRef = collection(db, 'posts');
    const q = query(postsRef, where('userId', '==', userId));
    const querySnapshot = await getDocs(q);
    const posts = querySnapshot.docs.map(doc => doc.data());
    return posts;
}

// API endpoint to get user's posts
app.post('/getUserPosts', async (req, res) => {
    const { email, password } = req.body;

    try {
        // Authenticate the user
        const userCredential = await signInWithEmailAndPassword(auth, email, password);
        const user = userCredential.user;

        // Fetch posts
        const posts = await fetchUserPosts(user.uid);

        // Save posts to a JSON file
        fs.writeFileSync('userPosts.json', JSON.stringify(posts, null, 2));
        res.send({ message: 'Posts fetched successfully', posts });
    } catch (error) {
        console.error('Error fetching user posts:', error);
        res.status(500).send({ message: 'Failed to fetch user posts' });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
