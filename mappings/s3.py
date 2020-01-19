class AWSS3BucketPermissions:
    def get_permissions(self, resname, res):
        bucketname = self._get_property_or_default(res, "*", "BucketName")
        accesscontrol = self._get_property_or_default(res, None, "AccessControl")
        analyticsconfigurations_len = self._get_property_array_length(res, None, "AnalyticsConfigurations")
        bucketencryption_len = self._get_property_array_length(res, None, "BucketEncryption", "ServerSideEncryptionConfiguration")
        corsconfiguration_len = self._get_property_array_length(res, None, "CorsConfiguration", "CorsRules")
        accelerateconfiguration = self._get_property_or_default(res, None, "AccelerateConfiguration", "AccelerationStatus")
        inventoryconfigurations_len = self._get_property_array_length(res, None, "InventoryConfigurations")
        lifecycleconfiguration_len = self._get_property_array_length(res, None, "LifecycleConfiguration", "Rules")
        loggingconfiguration_exists = self._get_property_exists(res, "LoggingConfiguration")
        metricsconfigurations_len = self._get_property_array_length(res, None, "MetricsConfigurations")
        notificationconfiguration_exists = self._get_property_exists(res, "NotificationConfiguration")
        objectlockconfiguration_exists = self._get_property_exists(res, "ObjectLockConfiguration")
        objectlockenabled = self._get_property_or_default(res, False, "ObjectLockEnabled")
        publicaccessblockonfiguration_exists = self._get_property_exists(res, "PublicAccessBlockConfiguration")
        versioningconfiguration = self._get_property_or_default(res, None, "VersioningConfiguration", "Status")
        websiteconfiguration_exists = self._get_property_exists(res, "WebsiteConfiguration")
        replicationconfigurationrole = self._get_property_or_default(res, None, "ReplicationConfiguration", "Role")

        self.permissions.add(
            resname=resname,
            lifecycle='Create',
            actions=[
                's3:CreateBucket'
            ],
            resources=[
                'arn:aws:s3:::{}'.format(bucketname)
            ]
        )
        if accesscontrol:
            self.permissions.add(
                resname=resname,
                lifecycle='Create',
                actions=[
                    's3:PutBucketAcl'
                ],
                resources=[
                    'arn:aws:s3:::{}'.format(bucketname)
                ]
            )
        if analyticsconfigurations_len:
            self.permissions.add(
                resname=resname,
                lifecycle='Create',
                actions=[
                    's3:PutAnalyticsConfiguration'
                ],
                resources=[
                    'arn:aws:s3:::{}'.format(bucketname)
                ]
            )
        if bucketencryption_len:
            self.permissions.add(
                resname=resname,
                lifecycle='Create',
                actions=[
                    's3:PutEncryptionConfiguration'
                ],
                resources=[
                    'arn:aws:s3:::{}'.format(bucketname)
                ]
            )
        if corsconfiguration_len:
            self.permissions.add(
                resname=resname,
                lifecycle='Create',
                actions=[
                    's3:PutBucketCORS'
                ],
                resources=[
                    'arn:aws:s3:::{}'.format(bucketname)
                ]
            )
        if accelerateconfiguration:
            self.permissions.add(
                resname=resname,
                lifecycle='Create',
                actions=[
                    's3:PutAccelerateConfiguration'
                ],
                resources=[
                    'arn:aws:s3:::{}'.format(bucketname)
                ]
            )
        if inventoryconfigurations_len:
            self.permissions.add(
                resname=resname,
                lifecycle='Create',
                actions=[
                    's3:PutInventoryConfiguration'
                ],
                resources=[
                    'arn:aws:s3:::{}'.format(bucketname)
                ]
            )
        if lifecycleconfiguration_len:
            self.permissions.add(
                resname=resname,
                lifecycle='Create',
                actions=[
                    's3:PutLifecycleConfiguration'
                ],
                resources=[
                    'arn:aws:s3:::{}'.format(bucketname)
                ]
            )
        if loggingconfiguration_exists:
            self.permissions.add(
                resname=resname,
                lifecycle='Create',
                actions=[
                    's3:PutBucketLogging'
                ],
                resources=[
                    'arn:aws:s3:::{}'.format(bucketname)
                ]
            )
        if metricsconfigurations_len:
            self.permissions.add(
                resname=resname,
                lifecycle='Create',
                actions=[
                    's3:PutMetricsConfiguration'
                ],
                resources=[
                    'arn:aws:s3:::{}'.format(bucketname)
                ]
            )
        if notificationconfiguration_exists:
            self.permissions.add(
                resname=resname,
                lifecycle='Create',
                actions=[
                    's3:PutBucketNotification'
                ],
                resources=[
                    'arn:aws:s3:::{}'.format(bucketname)
                ]
            )
        if objectlockconfiguration_exists or objectlockenabled:
            self.permissions.add(
                resname=resname,
                lifecycle='Create',
                actions=[
                    's3:PutBucketObjectLockConfiguration'
                ],
                resources=[
                    'arn:aws:s3:::{}'.format(bucketname)
                ]
            )
        if publicaccessblockonfiguration_exists:
            self.permissions.add(
                resname=resname,
                lifecycle='Create',
                actions=[
                    's3:PutBucketPublicAccessBlock'
                ],
                resources=[
                    'arn:aws:s3:::{}'.format(bucketname)
                ]
            )
        if versioningconfiguration:
            self.permissions.add(
                resname=resname,
                lifecycle='Create',
                actions=[
                    's3:PutBucketVersioning'
                ],
                resources=[
                    'arn:aws:s3:::{}'.format(bucketname)
                ]
            )
        if websiteconfiguration_exists:
            self.permissions.add(
                resname=resname,
                lifecycle='Create',
                actions=[
                    's3:PutBucketWebsite'
                ],
                resources=[
                    'arn:aws:s3:::{}'.format(bucketname)
                ]
            )
        if replicationconfigurationrole:
            self.permissions.add(
                resname=resname,
                lifecycle='Create',
                actions=[
                    's3:PutReplicationConfiguration'
                ],
                resources=[
                    'arn:aws:s3:::{}'.format(bucketname)
                ]
            )
            self.permissions.add(
                resname=resname,
                lifecycle='Create',
                actions=[
                    'iam:PassRole'
                ],
                resources=[
                    replicationconfigurationrole
                ],
                conditions={
                    'StringEquals': {
                        'iam:PassedToService': 's3.amazonaws.com'
                    }
                }
            )
        self.permissions.add(
            resname=resname,
            lifecycle='Delete',
            actions=[
                's3:DeleteBucket'
            ],
            resources=[
                'arn:aws:s3:::{}'.format(bucketname)
            ]
        )