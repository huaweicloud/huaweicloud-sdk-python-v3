# coding: utf-8

import pprint
import re

import six





class QuotaList:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'backup_gigabytes': 'QuotaDetailBackupGigabytes',
        'backups': 'QuotaDetailBackups',
        'gigabytes': 'QuotaDetailGigabytes',
        'id': 'str',
        'snapshots': 'QuotaDetailSnapshots',
        'volumes': 'QuotaDetailVolumes',
        'gigabytes_sata': 'QuotaDetailGigabytesSATA',
        'snapshots_sata': 'QuotaDetailSnapshotsSATA',
        'volumes_sata': 'QuotaDetailVolumesSATA',
        'gigabytes_sas': 'QuotaDetailGigabytesSAS',
        'snapshots_sas': 'QuotaDetailSnapshotsSAS',
        'volumes_sas': 'QuotaDetailVolumesSAS',
        'gigabytes_ssd': 'QuotaDetailGigabytesSSD',
        'snapshots_ssd': 'QuotaDetailSnapshotsSSD',
        'volumes_ssd': 'QuotaDetailVolumesSSD',
        'gigabytes_gpssd': 'QuotaDetailGigabytesGPSSD',
        'snapshots_gpssd': 'QuotaDetailSnapshotsGPSSD',
        'volumes_gpssd': 'QuotaDetailVolumesGPSSD',
        'per_volume_gigabytes': 'QuotaDetailPerVolumeGigabytes'
    }

    attribute_map = {
        'backup_gigabytes': 'backup_gigabytes',
        'backups': 'backups',
        'gigabytes': 'gigabytes',
        'id': 'id',
        'snapshots': 'snapshots',
        'volumes': 'volumes',
        'gigabytes_sata': 'gigabytes_SATA',
        'snapshots_sata': 'snapshots_SATA',
        'volumes_sata': 'volumes_SATA',
        'gigabytes_sas': 'gigabytes_SAS',
        'snapshots_sas': 'snapshots_SAS',
        'volumes_sas': 'volumes_SAS',
        'gigabytes_ssd': 'gigabytes_SSD',
        'snapshots_ssd': 'snapshots_SSD',
        'volumes_ssd': 'volumes_SSD',
        'gigabytes_gpssd': 'gigabytes_GPSSD',
        'snapshots_gpssd': 'snapshots_GPSSD',
        'volumes_gpssd': 'volumes_GPSSD',
        'per_volume_gigabytes': 'per_volume_gigabytes'
    }

    def __init__(self, backup_gigabytes=None, backups=None, gigabytes=None, id=None, snapshots=None, volumes=None, gigabytes_sata=None, snapshots_sata=None, volumes_sata=None, gigabytes_sas=None, snapshots_sas=None, volumes_sas=None, gigabytes_ssd=None, snapshots_ssd=None, volumes_ssd=None, gigabytes_gpssd=None, snapshots_gpssd=None, volumes_gpssd=None, per_volume_gigabytes=None):
        """QuotaList - a model defined in huaweicloud sdk"""
        
        

        self._backup_gigabytes = None
        self._backups = None
        self._gigabytes = None
        self._id = None
        self._snapshots = None
        self._volumes = None
        self._gigabytes_sata = None
        self._snapshots_sata = None
        self._volumes_sata = None
        self._gigabytes_sas = None
        self._snapshots_sas = None
        self._volumes_sas = None
        self._gigabytes_ssd = None
        self._snapshots_ssd = None
        self._volumes_ssd = None
        self._gigabytes_gpssd = None
        self._snapshots_gpssd = None
        self._volumes_gpssd = None
        self._per_volume_gigabytes = None
        self.discriminator = None

        self.backup_gigabytes = backup_gigabytes
        self.backups = backups
        self.gigabytes = gigabytes
        self.id = id
        self.snapshots = snapshots
        self.volumes = volumes
        if gigabytes_sata is not None:
            self.gigabytes_sata = gigabytes_sata
        if snapshots_sata is not None:
            self.snapshots_sata = snapshots_sata
        if volumes_sata is not None:
            self.volumes_sata = volumes_sata
        if gigabytes_sas is not None:
            self.gigabytes_sas = gigabytes_sas
        if snapshots_sas is not None:
            self.snapshots_sas = snapshots_sas
        if volumes_sas is not None:
            self.volumes_sas = volumes_sas
        if gigabytes_ssd is not None:
            self.gigabytes_ssd = gigabytes_ssd
        if snapshots_ssd is not None:
            self.snapshots_ssd = snapshots_ssd
        if volumes_ssd is not None:
            self.volumes_ssd = volumes_ssd
        if gigabytes_gpssd is not None:
            self.gigabytes_gpssd = gigabytes_gpssd
        if snapshots_gpssd is not None:
            self.snapshots_gpssd = snapshots_gpssd
        if volumes_gpssd is not None:
            self.volumes_gpssd = volumes_gpssd
        if per_volume_gigabytes is not None:
            self.per_volume_gigabytes = per_volume_gigabytes

    @property
    def backup_gigabytes(self):
        """Gets the backup_gigabytes of this QuotaList.


        :return: The backup_gigabytes of this QuotaList.
        :rtype: QuotaDetailBackupGigabytes
        """
        return self._backup_gigabytes

    @backup_gigabytes.setter
    def backup_gigabytes(self, backup_gigabytes):
        """Sets the backup_gigabytes of this QuotaList.


        :param backup_gigabytes: The backup_gigabytes of this QuotaList.
        :type: QuotaDetailBackupGigabytes
        """
        self._backup_gigabytes = backup_gigabytes

    @property
    def backups(self):
        """Gets the backups of this QuotaList.


        :return: The backups of this QuotaList.
        :rtype: QuotaDetailBackups
        """
        return self._backups

    @backups.setter
    def backups(self, backups):
        """Sets the backups of this QuotaList.


        :param backups: The backups of this QuotaList.
        :type: QuotaDetailBackups
        """
        self._backups = backups

    @property
    def gigabytes(self):
        """Gets the gigabytes of this QuotaList.


        :return: The gigabytes of this QuotaList.
        :rtype: QuotaDetailGigabytes
        """
        return self._gigabytes

    @gigabytes.setter
    def gigabytes(self, gigabytes):
        """Sets the gigabytes of this QuotaList.


        :param gigabytes: The gigabytes of this QuotaList.
        :type: QuotaDetailGigabytes
        """
        self._gigabytes = gigabytes

    @property
    def id(self):
        """Gets the id of this QuotaList.

        项目ID。

        :return: The id of this QuotaList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuotaList.

        项目ID。

        :param id: The id of this QuotaList.
        :type: str
        """
        self._id = id

    @property
    def snapshots(self):
        """Gets the snapshots of this QuotaList.


        :return: The snapshots of this QuotaList.
        :rtype: QuotaDetailSnapshots
        """
        return self._snapshots

    @snapshots.setter
    def snapshots(self, snapshots):
        """Sets the snapshots of this QuotaList.


        :param snapshots: The snapshots of this QuotaList.
        :type: QuotaDetailSnapshots
        """
        self._snapshots = snapshots

    @property
    def volumes(self):
        """Gets the volumes of this QuotaList.


        :return: The volumes of this QuotaList.
        :rtype: QuotaDetailVolumes
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this QuotaList.


        :param volumes: The volumes of this QuotaList.
        :type: QuotaDetailVolumes
        """
        self._volumes = volumes

    @property
    def gigabytes_sata(self):
        """Gets the gigabytes_sata of this QuotaList.


        :return: The gigabytes_sata of this QuotaList.
        :rtype: QuotaDetailGigabytesSATA
        """
        return self._gigabytes_sata

    @gigabytes_sata.setter
    def gigabytes_sata(self, gigabytes_sata):
        """Sets the gigabytes_sata of this QuotaList.


        :param gigabytes_sata: The gigabytes_sata of this QuotaList.
        :type: QuotaDetailGigabytesSATA
        """
        self._gigabytes_sata = gigabytes_sata

    @property
    def snapshots_sata(self):
        """Gets the snapshots_sata of this QuotaList.


        :return: The snapshots_sata of this QuotaList.
        :rtype: QuotaDetailSnapshotsSATA
        """
        return self._snapshots_sata

    @snapshots_sata.setter
    def snapshots_sata(self, snapshots_sata):
        """Sets the snapshots_sata of this QuotaList.


        :param snapshots_sata: The snapshots_sata of this QuotaList.
        :type: QuotaDetailSnapshotsSATA
        """
        self._snapshots_sata = snapshots_sata

    @property
    def volumes_sata(self):
        """Gets the volumes_sata of this QuotaList.


        :return: The volumes_sata of this QuotaList.
        :rtype: QuotaDetailVolumesSATA
        """
        return self._volumes_sata

    @volumes_sata.setter
    def volumes_sata(self, volumes_sata):
        """Sets the volumes_sata of this QuotaList.


        :param volumes_sata: The volumes_sata of this QuotaList.
        :type: QuotaDetailVolumesSATA
        """
        self._volumes_sata = volumes_sata

    @property
    def gigabytes_sas(self):
        """Gets the gigabytes_sas of this QuotaList.


        :return: The gigabytes_sas of this QuotaList.
        :rtype: QuotaDetailGigabytesSAS
        """
        return self._gigabytes_sas

    @gigabytes_sas.setter
    def gigabytes_sas(self, gigabytes_sas):
        """Sets the gigabytes_sas of this QuotaList.


        :param gigabytes_sas: The gigabytes_sas of this QuotaList.
        :type: QuotaDetailGigabytesSAS
        """
        self._gigabytes_sas = gigabytes_sas

    @property
    def snapshots_sas(self):
        """Gets the snapshots_sas of this QuotaList.


        :return: The snapshots_sas of this QuotaList.
        :rtype: QuotaDetailSnapshotsSAS
        """
        return self._snapshots_sas

    @snapshots_sas.setter
    def snapshots_sas(self, snapshots_sas):
        """Sets the snapshots_sas of this QuotaList.


        :param snapshots_sas: The snapshots_sas of this QuotaList.
        :type: QuotaDetailSnapshotsSAS
        """
        self._snapshots_sas = snapshots_sas

    @property
    def volumes_sas(self):
        """Gets the volumes_sas of this QuotaList.


        :return: The volumes_sas of this QuotaList.
        :rtype: QuotaDetailVolumesSAS
        """
        return self._volumes_sas

    @volumes_sas.setter
    def volumes_sas(self, volumes_sas):
        """Sets the volumes_sas of this QuotaList.


        :param volumes_sas: The volumes_sas of this QuotaList.
        :type: QuotaDetailVolumesSAS
        """
        self._volumes_sas = volumes_sas

    @property
    def gigabytes_ssd(self):
        """Gets the gigabytes_ssd of this QuotaList.


        :return: The gigabytes_ssd of this QuotaList.
        :rtype: QuotaDetailGigabytesSSD
        """
        return self._gigabytes_ssd

    @gigabytes_ssd.setter
    def gigabytes_ssd(self, gigabytes_ssd):
        """Sets the gigabytes_ssd of this QuotaList.


        :param gigabytes_ssd: The gigabytes_ssd of this QuotaList.
        :type: QuotaDetailGigabytesSSD
        """
        self._gigabytes_ssd = gigabytes_ssd

    @property
    def snapshots_ssd(self):
        """Gets the snapshots_ssd of this QuotaList.


        :return: The snapshots_ssd of this QuotaList.
        :rtype: QuotaDetailSnapshotsSSD
        """
        return self._snapshots_ssd

    @snapshots_ssd.setter
    def snapshots_ssd(self, snapshots_ssd):
        """Sets the snapshots_ssd of this QuotaList.


        :param snapshots_ssd: The snapshots_ssd of this QuotaList.
        :type: QuotaDetailSnapshotsSSD
        """
        self._snapshots_ssd = snapshots_ssd

    @property
    def volumes_ssd(self):
        """Gets the volumes_ssd of this QuotaList.


        :return: The volumes_ssd of this QuotaList.
        :rtype: QuotaDetailVolumesSSD
        """
        return self._volumes_ssd

    @volumes_ssd.setter
    def volumes_ssd(self, volumes_ssd):
        """Sets the volumes_ssd of this QuotaList.


        :param volumes_ssd: The volumes_ssd of this QuotaList.
        :type: QuotaDetailVolumesSSD
        """
        self._volumes_ssd = volumes_ssd

    @property
    def gigabytes_gpssd(self):
        """Gets the gigabytes_gpssd of this QuotaList.


        :return: The gigabytes_gpssd of this QuotaList.
        :rtype: QuotaDetailGigabytesGPSSD
        """
        return self._gigabytes_gpssd

    @gigabytes_gpssd.setter
    def gigabytes_gpssd(self, gigabytes_gpssd):
        """Sets the gigabytes_gpssd of this QuotaList.


        :param gigabytes_gpssd: The gigabytes_gpssd of this QuotaList.
        :type: QuotaDetailGigabytesGPSSD
        """
        self._gigabytes_gpssd = gigabytes_gpssd

    @property
    def snapshots_gpssd(self):
        """Gets the snapshots_gpssd of this QuotaList.


        :return: The snapshots_gpssd of this QuotaList.
        :rtype: QuotaDetailSnapshotsGPSSD
        """
        return self._snapshots_gpssd

    @snapshots_gpssd.setter
    def snapshots_gpssd(self, snapshots_gpssd):
        """Sets the snapshots_gpssd of this QuotaList.


        :param snapshots_gpssd: The snapshots_gpssd of this QuotaList.
        :type: QuotaDetailSnapshotsGPSSD
        """
        self._snapshots_gpssd = snapshots_gpssd

    @property
    def volumes_gpssd(self):
        """Gets the volumes_gpssd of this QuotaList.


        :return: The volumes_gpssd of this QuotaList.
        :rtype: QuotaDetailVolumesGPSSD
        """
        return self._volumes_gpssd

    @volumes_gpssd.setter
    def volumes_gpssd(self, volumes_gpssd):
        """Sets the volumes_gpssd of this QuotaList.


        :param volumes_gpssd: The volumes_gpssd of this QuotaList.
        :type: QuotaDetailVolumesGPSSD
        """
        self._volumes_gpssd = volumes_gpssd

    @property
    def per_volume_gigabytes(self):
        """Gets the per_volume_gigabytes of this QuotaList.


        :return: The per_volume_gigabytes of this QuotaList.
        :rtype: QuotaDetailPerVolumeGigabytes
        """
        return self._per_volume_gigabytes

    @per_volume_gigabytes.setter
    def per_volume_gigabytes(self, per_volume_gigabytes):
        """Sets the per_volume_gigabytes of this QuotaList.


        :param per_volume_gigabytes: The per_volume_gigabytes of this QuotaList.
        :type: QuotaDetailPerVolumeGigabytes
        """
        self._per_volume_gigabytes = per_volume_gigabytes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QuotaList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
