from setuptools import setup

package_name = 'eve_hands'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ahgo',
    maintainer_email='a.h.g.overbeek@utwente.nl',
    description='Controlling bebionic programatically',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'wave_r.py = eve_hands.publisher_member_function:main',
            'wave_rl.py = eve_hands.wave_rl:main',
            'rock_on.py = eve_hands.rock_on:main',
            'open.py = eve_hands.open:main',
            'close.py = eve_hands.close:main',
            'listener.py = eve_hands.subscriber_member_function:main',
        ],
    },
)
