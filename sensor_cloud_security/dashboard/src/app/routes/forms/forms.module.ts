import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SelectModule } from 'ng2-select';
import { TextMaskModule } from 'angular2-text-mask';
import { CustomFormsModule } from 'ng2-validation';
import { FileUploadModule } from 'ng2-file-upload';

import { SharedModule } from '../../shared/shared.module';
import { MonitorComponent } from './monitor/monitor.component';
import { DeployComponent } from './deploy/deploy.component';

const routes: Routes = [
    { path: 'monitor', component: MonitorComponent },
    { path: 'deploy', component: DeployComponent }
];

@NgModule({
    imports: [
        SharedModule,
        RouterModule.forChild(routes),
        SelectModule,
        TextMaskModule,
        CustomFormsModule,
        FileUploadModule,
    ],
    providers: [],
    declarations: [
        MonitorComponent,
        DeployComponent
    ],
    exports: [
        RouterModule
    ]
})
export class FormsModule { }
