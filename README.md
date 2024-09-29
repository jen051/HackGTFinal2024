# Inspiration/Purpose

Violence is an ongoing global issue, disproportionately impacting women and marginalized groups in particular. Many face threats to their safety in their day-to-day life, making knowledge about self-defense not only empowering but also life-saving. Our project, Fight and Furious, is driven by the current reality that too many individuals, including close friends and family, could have benefited from these practical self-defense skills. To further this cause, we chose Krav Maga as the core technique our app will be teaching due to its proven effectiveness in self-defense in the real world. One team member on our team always had a passion and interest in Krav Maga after participating in the Krav Maga classes offered at the Georgia Tech Campus Recreation Center. Through further discussions with the team about recent dangerous incidents in Downtown Atlanta and the forever-lingering fear of one day experiencing those threats as young girls, we decided to do our part as students interested in Computer Science to contribute to the fight against gender-based violence. This inspired us to create Fight and Furious, an app that provides an accessible and easy-to-follow self-defense education. As a readily available resource that can be used on any mobile device, our goal is to ensure that everyone has access to the knowledge to protect themselves during times of need.

# Process

Built with React, the user interface offers an interactive experience, featuring informational context about Krav Maga. During the development process, we sketched UI layouts that combined our creative ideas and ensured that the aesthetics of the app made the intimidating Krav Maga technique into something approachable to anyone. For instance, the Home page of Fight and Furious includes an eye-catching title with a soft and welcoming character like a panda. Our team split up into two pairs to work on backend Python work and frontend React work separately, and later embedded the computer vision model that calculates how accurately the user performs each Krav Maga technique into the React space. With teammates who have minimal experience in web development, ML models, and computer vision, we jumped at the opportunity to learn more about these concepts. Using the help of various 5-minute YouTube tutorials of HTML and supportive mentors, we absorbed knowledge quickly, and as a result, we were able to successfully create a working visualization of our self-teaching Krav Maga web app. Additionally, to test our model and calculations, we approached several participants to experiment with the app and investigated factors that were affecting the accuracy of the model such as the lighting of the room or the type of clothing item the user was wearing. By integrating feedback from participants, we were able to maximize the accuracy rate of the app and incorporate designs and encouraging messages like “Congratulations” to help users master Krav Maga techniques efficiently and more importantly, keep learning fun.

# Challenges

Throughout our project, we encountered several significant challenges:

**1. Position Accuracy Logistics**
There are many ways to calculate the difference in a person’s position in two images. However, it was up to us to determine which method was the best approach. Initially, we took the naive approach by calculating the difference between each of the observed and the reference joint positions. As our understanding evolved, we researched and discovered better methods of calculating error and accuracy. Eventually, we determined that the most mathematically sensible way to compute accuracy is to calculate the MSE of angles between vectorized limbs.

**2. Backend to Frontend Communication**
Relaying a backend model of live video analysis to a frontend web page proved to be challenging, as we needed to display the live video with analyzed accuracy data and more. Traditionally, we would relay the stream frame-by-frame. Due to time constraints, we decided to learn to use the streamlit library and embed our live video as an iframe in our webpage. Overcoming this challenge was an excellent learning experience and a test of our adaptivity and creativity.

**3. Lack of Experience**
We decided to use computer vision in our program, but no one in our team has worked with computer vision before. Our unfamiliarity with motion tracking and pose detection models such as MediaPipe made implementing the backend vision model quite challenging. Additionally, our team had little to no front end development experience. Our overall lack of experience may have temporarily hindered our development progress, but through our collaboration and resourcefulness, we were able to overcome these difficulties and gain valuable hands-on experience.
Navigating through these challenges demanded adaptability, collaboration, and perseverance from our team. Despite the hurdles, our collective efforts enabled us to make significant progress and achieve our project objectives, which as a team, grew our confidence in taking on larger projects in the future.

# Accomplishments/What we learned

Throughout this hackathon, our team gained valuable insight and knowledge across both technical and social capabilities. One key takeaway was understanding the difference between pose detection and pose classification while self-teaching ourselves about computer vision. This distinction was important to recognize because this is what allowed us to refine how our app interprets user movements in real-time. Additionally, we learned how to effectively use React.js, working with components to display embedded media like images and videos to enhance the accessibility and interactivity of the user interface as a whole. Our team collectively learned how to design interactive, responsive applications and how to maintain a clean structure. Moreover, researching statistics on gender violence helped us realize the seriousness of the issue, showing how widespread and urgent the problem at hand is. The fact that over 736 million women have faced some sort of gender violence in their lives and that almost 26% of those women are from ages 15 to 24 was alarming and saddening to hear. This knowledge fueled our passion to complete Fight and Furious, and it became a meaningful effort for all of our teammates that we were able to address a critical social issue. Lastly, on a teamwork level, each team member sharpened our collaboration, communication, and time management skills. By delegating tasks to members who were more proficient in certain skills and receiving regular feedback during coding sessions, we accomplished the goal of completing our final product and working together without any conflicts--all of which are skills that are essential for us in a future workplace setting.  

# Future improvements
**Real-Time Form Analysis & Feedback:** Refine motion tracking algorithm by training our own Krav Maga data set to provide live feedback on users’ form and technique execution to highlight areas for improvement and guide users to helping them master techniques more quickly.

**Expanding Techniques:** Implement a wider range of Krav Maga techniques such as Choke Escapes and Back Kicks.

**Personalized Training:** Factor in users’ unique physical attributes such as different heights, weights, flexibility, and strength to personalize training. 

**Interactive VR/AR Activities:** Allow users to practice their Krav Maga techniques in real-world simulations by integrating virtual or augmented reality features to provide hands-on training.

**Increased Accessibility:** Collaborate with local communities and organizations, particularly to those who lack access to self-defense resources to offer a no-cost educational tool for anyone to use and learn essential self-defense education.

---------------------------------

# Contributors

Mae Chen, GitHub Username @maechen

Jennifier Jiang, GitHub Username @jen051

Kat Jeong, GitHub Username @suhinjeong

Michelle Park, GitHub Username @park.yj.michelle@gmail.com
