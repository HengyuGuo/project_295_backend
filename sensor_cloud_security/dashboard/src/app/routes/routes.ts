import { LayoutComponent } from '../layout/layout.component';
import {MyAccountComponent} from '../my-account/my-account.component';

export const routes = [
    {
		path: '',
		redirectTo: '/home',
		pathMatch: 'full'
	},

    {
		path: 'myAccount',
		component: MyAccountComponent
	},

    {
        path: '',
        component: LayoutComponent,
        children: [
            { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
            { path: 'dashboard', loadChildren: './dashboard/dashboard.module#DashboardModule' },
            { path: 'widgets', loadChildren: './widgets/widgets.module#WidgetsModule' },
            { path: 'forms', loadChildren: './forms/forms.module#FormsModule' },
            { path: 'charts', loadChildren: './charts/charts.module#ChartsModule' },
            { path: 'maps', loadChildren: './maps/maps.module#MapsModule' }
        ]
    },


    // Not found
    { path: '**', redirectTo: 'myAccount' }

];
