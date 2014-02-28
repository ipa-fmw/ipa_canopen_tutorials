// ROS includes
#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
#include <dynamic_reconfigure/server.h>
#include <ipa_canopen_deployment_test/torso_testConfig.h>

// ROS message includes
#include <brics_actuator/JointVelocities.h>




#include <torso_test_common.cpp>


class torso_test_ros
{
	public:
		ros::NodeHandle n_;
		
		dynamic_reconfigure::Server<ipa_canopen_deployment_test::torso_testConfig> server;
  		dynamic_reconfigure::Server<ipa_canopen_deployment_test::torso_testConfig>::CallbackType f;
		

		ros::Publisher command_vel_;
		

        
 
        torso_test_data component_data_;
        torso_test_config component_config_;
        torso_test_impl component_implementation_;

        torso_test_ros()
        {
       	
  			f = boost::bind(&torso_test_ros::configure_callback, this, _1, _2);
  			server.setCallback(f);
        	
        
				command_vel_ = 	n_.advertise<brics_actuator::JointVelocities>("command_vel", 1);
  	

            
        }
        
		
		void configure_callback(ipa_canopen_deployment_test::torso_testConfig &config, uint32_t level) 
		{
		}

        void configure()
        {
			component_implementation_.configure(component_config_);
        }

        void update()
        {
            component_implementation_.update(component_data_, component_config_);
				command_vel_.publish(component_data_.out_command_vel);
    
        }
 
};

int main(int argc, char** argv)
{

	ros::init(argc, argv, "torso_test");

	torso_test_ros node;
    node.configure();

	
 	ros::Rate loop_rate(0.2); // Hz

	while(node.n_.ok())
	{
        node.update();
		loop_rate.sleep();
		ros::spinOnce();
	}
	
    return 0;
}
