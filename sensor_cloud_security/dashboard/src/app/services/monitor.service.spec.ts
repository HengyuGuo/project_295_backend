/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { MonitorService } from './monitor.service';

describe('MonitorService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [MonitorService]
    });
  });

  it('should ...', inject([MonitorService], (service: MonitorService) => {
    expect(service).toBeTruthy();
  }));
});
