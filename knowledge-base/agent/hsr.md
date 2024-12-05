# HSR information

### HSR Robot: Overview and Capabilities

The **HSR (Human Support Robot)** is a mobile manipulator developed by **Toyota Research Institute**, first introduced in **2012** as part of Toyota’s efforts to create assistive robots for aging populations and individuals with limited mobility. HSR is designed to operate in domestic and healthcare environments, performing tasks that enhance daily living and improve quality of life.

#### Physical Specifications:
- **Arms and Hands:**
  - HSR features a single **5-DOF robotic arm** with a multi-fingered gripper. The gripper can handle objects of varying shapes and sizes, making it versatile for everyday tasks.
- **Base and Mobility:**
  - The robot is equipped with a **wheeled omnidirectional base**, enabling smooth navigation and precise positioning in cluttered or constrained indoor spaces.
- **Joints:**
  - HSR has **8 degrees of freedom (8-DOF)** distributed across its arm, base, and pan-tilt head.
- **Sensors:**
  - It includes an advanced sensor suite:
    - A **RGB-D camera** for object detection and 3D mapping.
    - Laser range finders for localization and obstacle avoidance.
    - A microphone and speaker for audio interaction.
    - Force sensors in the arm for safe manipulation.
- **Adjustable Height:**
  - HSR has a telescopic torso that can adjust its height to reach objects at different levels, enhancing its operational flexibility.

#### Technical Capabilities:
- **Tasks:**
  - HSR is capable of performing a wide range of tasks, such as:
    - Fetching and delivering items like drinks, tools, or personal belongings.
    - Picking up objects from the floor, tables, or shelves.
    - Opening doors and operating light switches.
    - Interacting with people via voice commands or touch interfaces.
  - Its ability to autonomously detect and manipulate objects makes it particularly useful in domestic and healthcare environments.
- **Customizability:**
  - HSR is powered by **ROS (Robot Operating System)**, allowing developers to modify its software and experiment with advanced AI algorithms, including vision, manipulation, and human-robot interaction modules.
- **Collaboration:**
  - Designed for safe operation around people, HSR has integrated compliance control and collision avoidance, ensuring a safe and efficient collaboration in shared environments.

#### Limitations:
- **Tasks:**
  - At the moment HSR can not perform wiping task
  - At the moment HSR can not perform picking up object from floor task
  
#### Applications and Legacy:
The HSR has been adopted by researchers globally to explore areas such as assistive robotics, autonomous navigation, and interactive task learning. Its compact design, user-friendly interface, and ability to perform meaningful tasks make it a significant step forward in the development of robots aimed at improving human life, especially for individuals with physical limitations.