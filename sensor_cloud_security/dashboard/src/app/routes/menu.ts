
const Dashboard = {
    text: 'Dashboard',
    link: '/dashboard',
    icon: 'icon-speedometer',
    submenu: [
        {
            text: 'Dashbord v1',
            link: '/dashboard/v1'
        },
        {
            text: 'Dashbord v2',
            link: '/dashboard/v3'
        }
    ]
};

const PrivilegeManagement = {
    text: 'Privilege Management',
    link: '/widgets',
    icon: 'icon-people'
};

const SensorManagement = {
    text: 'Sensor Management',
    link: '/forms',
    icon: 'icon-note',
    submenu: [
        {
            text: 'Monitor',
            link: '/forms/monitor'
        },
        {
            text: 'Deploy',
            link: '/forms/deploy'
        }
    ]
};

const Analysis = {
    text: 'Big Data Analysis',
    link: '/charts',
    icon: 'icon-graph',
    submenu: [
        {
            text: 'A/C Management',
            link: '/charts/flot'
        },
        {
            text: 'WSN Monitor',
            link: '/charts/radial'
        },
        {
            text: 'System Setting',
            link: '/charts/setting'
        },
        {
            text: 'Cluster Monitor',
            link: '/charts/chartjs'
        }
    ]
};

const Maps = {
    text: 'Maps',
    link: '/maps',
    icon: 'icon-map',
    submenu: [
        {
            text: 'Google',
            link: '/maps/google'
        },
        {
            text: 'Vector',
            link: '/maps/vector'
        }
    ]
};

const headingMain = {
    text: 'Main Navigation',
    heading: true
};

const headingComponents = {
    text: 'Components',
    heading: true
};

const headingMore = {
    text: 'More',
    heading: true
};

export const menu = [
    headingMain,
    Dashboard,
    headingComponents,
    PrivilegeManagement,
    SensorManagement,
    Analysis,
    headingMore,
    Maps,
];
