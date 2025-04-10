# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CdmClusterDatastore:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'bigcluster_enable': 'bool',
        'default_version': 'str',
        'versions': 'list[CdmClusterVersion]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'bigcluster_enable': 'bigclusterEnable',
        'default_version': 'defaultVersion',
        'versions': 'versions'
    }

    def __init__(self, id=None, name=None, bigcluster_enable=None, default_version=None, versions=None):
        r"""CdmClusterDatastore

        The model defined in huaweicloud sdk

        :param id: 服务ID，用于区分不同服务。
        :type id: str
        :param name: 服务名称。
        :type name: str
        :param bigcluster_enable: 是否支持大规格集群。
        :type bigcluster_enable: bool
        :param default_version: 默认版本。
        :type default_version: str
        :param versions: 版本。
        :type versions: list[:class:`huaweicloudsdkcdm.v1.CdmClusterVersion`]
        """
        
        

        self._id = None
        self._name = None
        self._bigcluster_enable = None
        self._default_version = None
        self._versions = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.bigcluster_enable = bigcluster_enable
        self.default_version = default_version
        self.versions = versions

    @property
    def id(self):
        r"""Gets the id of this CdmClusterDatastore.

        服务ID，用于区分不同服务。

        :return: The id of this CdmClusterDatastore.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CdmClusterDatastore.

        服务ID，用于区分不同服务。

        :param id: The id of this CdmClusterDatastore.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CdmClusterDatastore.

        服务名称。

        :return: The name of this CdmClusterDatastore.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CdmClusterDatastore.

        服务名称。

        :param name: The name of this CdmClusterDatastore.
        :type name: str
        """
        self._name = name

    @property
    def bigcluster_enable(self):
        r"""Gets the bigcluster_enable of this CdmClusterDatastore.

        是否支持大规格集群。

        :return: The bigcluster_enable of this CdmClusterDatastore.
        :rtype: bool
        """
        return self._bigcluster_enable

    @bigcluster_enable.setter
    def bigcluster_enable(self, bigcluster_enable):
        r"""Sets the bigcluster_enable of this CdmClusterDatastore.

        是否支持大规格集群。

        :param bigcluster_enable: The bigcluster_enable of this CdmClusterDatastore.
        :type bigcluster_enable: bool
        """
        self._bigcluster_enable = bigcluster_enable

    @property
    def default_version(self):
        r"""Gets the default_version of this CdmClusterDatastore.

        默认版本。

        :return: The default_version of this CdmClusterDatastore.
        :rtype: str
        """
        return self._default_version

    @default_version.setter
    def default_version(self, default_version):
        r"""Sets the default_version of this CdmClusterDatastore.

        默认版本。

        :param default_version: The default_version of this CdmClusterDatastore.
        :type default_version: str
        """
        self._default_version = default_version

    @property
    def versions(self):
        r"""Gets the versions of this CdmClusterDatastore.

        版本。

        :return: The versions of this CdmClusterDatastore.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.CdmClusterVersion`]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this CdmClusterDatastore.

        版本。

        :param versions: The versions of this CdmClusterDatastore.
        :type versions: list[:class:`huaweicloudsdkcdm.v1.CdmClusterVersion`]
        """
        self._versions = versions

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CdmClusterDatastore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
