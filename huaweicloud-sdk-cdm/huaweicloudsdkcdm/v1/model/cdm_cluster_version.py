# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CdmClusterVersion:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'active': 'str',
        'id': 'str',
        'image': 'str',
        'name': 'str',
        'packages': 'str',
        'datastore': 'str',
        'links': 'list[ClusterLinks]'
    }

    attribute_map = {
        'active': 'active',
        'id': 'id',
        'image': 'image',
        'name': 'name',
        'packages': 'packages',
        'datastore': 'datastore',
        'links': 'links'
    }

    def __init__(self, active=None, id=None, image=None, name=None, packages=None, datastore=None, links=None):
        r"""CdmClusterVersion

        The model defined in huaweicloud sdk

        :param active: 版本状态。
        :type active: str
        :param id: 版本ID。
        :type id: str
        :param image: 版本镜像。
        :type image: str
        :param name: 版本名称。
        :type name: str
        :param packages: 版本的包。
        :type packages: str
        :param datastore: 服务ID，用于区分不同服务。
        :type datastore: str
        :param links: 链接信息。
        :type links: list[:class:`huaweicloudsdkcdm.v1.ClusterLinks`]
        """
        
        

        self._active = None
        self._id = None
        self._image = None
        self._name = None
        self._packages = None
        self._datastore = None
        self._links = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if id is not None:
            self.id = id
        if image is not None:
            self.image = image
        if name is not None:
            self.name = name
        if packages is not None:
            self.packages = packages
        if datastore is not None:
            self.datastore = datastore
        if links is not None:
            self.links = links

    @property
    def active(self):
        r"""Gets the active of this CdmClusterVersion.

        版本状态。

        :return: The active of this CdmClusterVersion.
        :rtype: str
        """
        return self._active

    @active.setter
    def active(self, active):
        r"""Sets the active of this CdmClusterVersion.

        版本状态。

        :param active: The active of this CdmClusterVersion.
        :type active: str
        """
        self._active = active

    @property
    def id(self):
        r"""Gets the id of this CdmClusterVersion.

        版本ID。

        :return: The id of this CdmClusterVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CdmClusterVersion.

        版本ID。

        :param id: The id of this CdmClusterVersion.
        :type id: str
        """
        self._id = id

    @property
    def image(self):
        r"""Gets the image of this CdmClusterVersion.

        版本镜像。

        :return: The image of this CdmClusterVersion.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this CdmClusterVersion.

        版本镜像。

        :param image: The image of this CdmClusterVersion.
        :type image: str
        """
        self._image = image

    @property
    def name(self):
        r"""Gets the name of this CdmClusterVersion.

        版本名称。

        :return: The name of this CdmClusterVersion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CdmClusterVersion.

        版本名称。

        :param name: The name of this CdmClusterVersion.
        :type name: str
        """
        self._name = name

    @property
    def packages(self):
        r"""Gets the packages of this CdmClusterVersion.

        版本的包。

        :return: The packages of this CdmClusterVersion.
        :rtype: str
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        r"""Sets the packages of this CdmClusterVersion.

        版本的包。

        :param packages: The packages of this CdmClusterVersion.
        :type packages: str
        """
        self._packages = packages

    @property
    def datastore(self):
        r"""Gets the datastore of this CdmClusterVersion.

        服务ID，用于区分不同服务。

        :return: The datastore of this CdmClusterVersion.
        :rtype: str
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this CdmClusterVersion.

        服务ID，用于区分不同服务。

        :param datastore: The datastore of this CdmClusterVersion.
        :type datastore: str
        """
        self._datastore = datastore

    @property
    def links(self):
        r"""Gets the links of this CdmClusterVersion.

        链接信息。

        :return: The links of this CdmClusterVersion.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.ClusterLinks`]
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this CdmClusterVersion.

        链接信息。

        :param links: The links of this CdmClusterVersion.
        :type links: list[:class:`huaweicloudsdkcdm.v1.ClusterLinks`]
        """
        self._links = links

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
        if not isinstance(other, CdmClusterVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
