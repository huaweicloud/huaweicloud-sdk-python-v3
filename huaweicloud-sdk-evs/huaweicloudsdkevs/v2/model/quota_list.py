# coding: utf-8

import pprint
import re

import six


class QuotaList(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'backup_gigabytes': 'QuotaDetail',
        'backups': 'QuotaDetail',
        'gigabytes': 'QuotaDetail',
        'id': 'str',
        'snapshots': 'QuotaDetail',
        'volumes': 'QuotaDetail',
        'volumes_ssd': 'QuotaDetail',
        'volumes_sas': 'QuotaDetail',
        'volumes_sata': 'QuotaDetail',
        'gigabytes_ssd': 'QuotaDetail',
        'gigabytes_sas': 'QuotaDetail',
        'gigabytes_sata': 'QuotaDetail',
        'snapshots_ssd': 'QuotaDetail',
        'snapshots_sas': 'QuotaDetail',
        'snapshots_sata': 'QuotaDetail'
    }

    attribute_map = {
        'backup_gigabytes': 'backup_gigabytes',
        'backups': 'backups',
        'gigabytes': 'gigabytes',
        'id': 'id',
        'snapshots': 'snapshots',
        'volumes': 'volumes',
        'volumes_ssd': 'volumes_SSD',
        'volumes_sas': 'volumes_SAS',
        'volumes_sata': 'volumes_SATA',
        'gigabytes_ssd': 'gigabytes_SSD',
        'gigabytes_sas': 'gigabytes_SAS',
        'gigabytes_sata': 'gigabytes_SATA',
        'snapshots_ssd': 'snapshots_SSD',
        'snapshots_sas': 'snapshots_SAS',
        'snapshots_sata': 'snapshots_SATA'
    }

    def __init__(self, backup_gigabytes=None, backups=None, gigabytes=None, id=None, snapshots=None, volumes=None, volumes_ssd=None, volumes_sas=None, volumes_sata=None, gigabytes_ssd=None, gigabytes_sas=None, gigabytes_sata=None, snapshots_ssd=None, snapshots_sas=None, snapshots_sata=None):  # noqa: E501
        """QuotaList - a model defined in huaweicloud sdk"""

        self._backup_gigabytes = None
        self._backups = None
        self._gigabytes = None
        self._id = None
        self._snapshots = None
        self._volumes = None
        self._volumes_ssd = None
        self._volumes_sas = None
        self._volumes_sata = None
        self._gigabytes_ssd = None
        self._gigabytes_sas = None
        self._gigabytes_sata = None
        self._snapshots_ssd = None
        self._snapshots_sas = None
        self._snapshots_sata = None
        self.discriminator = None

        self.backup_gigabytes = backup_gigabytes
        self.backups = backups
        self.gigabytes = gigabytes
        self.id = id
        self.snapshots = snapshots
        self.volumes = volumes
        if volumes_ssd is not None:
            self.volumes_ssd = volumes_ssd
        if volumes_sas is not None:
            self.volumes_sas = volumes_sas
        if volumes_sata is not None:
            self.volumes_sata = volumes_sata
        if gigabytes_ssd is not None:
            self.gigabytes_ssd = gigabytes_ssd
        if gigabytes_sas is not None:
            self.gigabytes_sas = gigabytes_sas
        if gigabytes_sata is not None:
            self.gigabytes_sata = gigabytes_sata
        if snapshots_ssd is not None:
            self.snapshots_ssd = snapshots_ssd
        if snapshots_sas is not None:
            self.snapshots_sas = snapshots_sas
        if snapshots_sata is not None:
            self.snapshots_sata = snapshots_sata

    @property
    def backup_gigabytes(self):
        """Gets the backup_gigabytes of this QuotaList.


        :return: The backup_gigabytes of this QuotaList.
        :rtype: QuotaDetail
        """
        return self._backup_gigabytes

    @backup_gigabytes.setter
    def backup_gigabytes(self, backup_gigabytes):
        """Sets the backup_gigabytes of this QuotaList.


        :param backup_gigabytes: The backup_gigabytes of this QuotaList.
        :type: QuotaDetail
        """
        self._backup_gigabytes = backup_gigabytes

    @property
    def backups(self):
        """Gets the backups of this QuotaList.


        :return: The backups of this QuotaList.
        :rtype: QuotaDetail
        """
        return self._backups

    @backups.setter
    def backups(self, backups):
        """Sets the backups of this QuotaList.


        :param backups: The backups of this QuotaList.
        :type: QuotaDetail
        """
        self._backups = backups

    @property
    def gigabytes(self):
        """Gets the gigabytes of this QuotaList.


        :return: The gigabytes of this QuotaList.
        :rtype: QuotaDetail
        """
        return self._gigabytes

    @gigabytes.setter
    def gigabytes(self, gigabytes):
        """Sets the gigabytes of this QuotaList.


        :param gigabytes: The gigabytes of this QuotaList.
        :type: QuotaDetail
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
        :rtype: QuotaDetail
        """
        return self._snapshots

    @snapshots.setter
    def snapshots(self, snapshots):
        """Sets the snapshots of this QuotaList.


        :param snapshots: The snapshots of this QuotaList.
        :type: QuotaDetail
        """
        self._snapshots = snapshots

    @property
    def volumes(self):
        """Gets the volumes of this QuotaList.


        :return: The volumes of this QuotaList.
        :rtype: QuotaDetail
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this QuotaList.


        :param volumes: The volumes of this QuotaList.
        :type: QuotaDetail
        """
        self._volumes = volumes

    @property
    def volumes_ssd(self):
        """Gets the volumes_ssd of this QuotaList.


        :return: The volumes_ssd of this QuotaList.
        :rtype: QuotaDetail
        """
        return self._volumes_ssd

    @volumes_ssd.setter
    def volumes_ssd(self, volumes_ssd):
        """Sets the volumes_ssd of this QuotaList.


        :param volumes_ssd: The volumes_ssd of this QuotaList.
        :type: QuotaDetail
        """
        self._volumes_ssd = volumes_ssd

    @property
    def volumes_sas(self):
        """Gets the volumes_sas of this QuotaList.


        :return: The volumes_sas of this QuotaList.
        :rtype: QuotaDetail
        """
        return self._volumes_sas

    @volumes_sas.setter
    def volumes_sas(self, volumes_sas):
        """Sets the volumes_sas of this QuotaList.


        :param volumes_sas: The volumes_sas of this QuotaList.
        :type: QuotaDetail
        """
        self._volumes_sas = volumes_sas

    @property
    def volumes_sata(self):
        """Gets the volumes_sata of this QuotaList.


        :return: The volumes_sata of this QuotaList.
        :rtype: QuotaDetail
        """
        return self._volumes_sata

    @volumes_sata.setter
    def volumes_sata(self, volumes_sata):
        """Sets the volumes_sata of this QuotaList.


        :param volumes_sata: The volumes_sata of this QuotaList.
        :type: QuotaDetail
        """
        self._volumes_sata = volumes_sata

    @property
    def gigabytes_ssd(self):
        """Gets the gigabytes_ssd of this QuotaList.


        :return: The gigabytes_ssd of this QuotaList.
        :rtype: QuotaDetail
        """
        return self._gigabytes_ssd

    @gigabytes_ssd.setter
    def gigabytes_ssd(self, gigabytes_ssd):
        """Sets the gigabytes_ssd of this QuotaList.


        :param gigabytes_ssd: The gigabytes_ssd of this QuotaList.
        :type: QuotaDetail
        """
        self._gigabytes_ssd = gigabytes_ssd

    @property
    def gigabytes_sas(self):
        """Gets the gigabytes_sas of this QuotaList.


        :return: The gigabytes_sas of this QuotaList.
        :rtype: QuotaDetail
        """
        return self._gigabytes_sas

    @gigabytes_sas.setter
    def gigabytes_sas(self, gigabytes_sas):
        """Sets the gigabytes_sas of this QuotaList.


        :param gigabytes_sas: The gigabytes_sas of this QuotaList.
        :type: QuotaDetail
        """
        self._gigabytes_sas = gigabytes_sas

    @property
    def gigabytes_sata(self):
        """Gets the gigabytes_sata of this QuotaList.


        :return: The gigabytes_sata of this QuotaList.
        :rtype: QuotaDetail
        """
        return self._gigabytes_sata

    @gigabytes_sata.setter
    def gigabytes_sata(self, gigabytes_sata):
        """Sets the gigabytes_sata of this QuotaList.


        :param gigabytes_sata: The gigabytes_sata of this QuotaList.
        :type: QuotaDetail
        """
        self._gigabytes_sata = gigabytes_sata

    @property
    def snapshots_ssd(self):
        """Gets the snapshots_ssd of this QuotaList.


        :return: The snapshots_ssd of this QuotaList.
        :rtype: QuotaDetail
        """
        return self._snapshots_ssd

    @snapshots_ssd.setter
    def snapshots_ssd(self, snapshots_ssd):
        """Sets the snapshots_ssd of this QuotaList.


        :param snapshots_ssd: The snapshots_ssd of this QuotaList.
        :type: QuotaDetail
        """
        self._snapshots_ssd = snapshots_ssd

    @property
    def snapshots_sas(self):
        """Gets the snapshots_sas of this QuotaList.


        :return: The snapshots_sas of this QuotaList.
        :rtype: QuotaDetail
        """
        return self._snapshots_sas

    @snapshots_sas.setter
    def snapshots_sas(self, snapshots_sas):
        """Sets the snapshots_sas of this QuotaList.


        :param snapshots_sas: The snapshots_sas of this QuotaList.
        :type: QuotaDetail
        """
        self._snapshots_sas = snapshots_sas

    @property
    def snapshots_sata(self):
        """Gets the snapshots_sata of this QuotaList.


        :return: The snapshots_sata of this QuotaList.
        :rtype: QuotaDetail
        """
        return self._snapshots_sata

    @snapshots_sata.setter
    def snapshots_sata(self, snapshots_sata):
        """Sets the snapshots_sata of this QuotaList.


        :param snapshots_sata: The snapshots_sata of this QuotaList.
        :type: QuotaDetail
        """
        self._snapshots_sata = snapshots_sata

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
