# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InterRegion:

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
        'project_id': 'str',
        'local_region_id': 'str',
        'remote_region_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'local_region_id': 'local_region_id',
        'remote_region_id': 'remote_region_id'
    }

    def __init__(self, id=None, project_id=None, local_region_id=None, remote_region_id=None):
        """InterRegion

        The model defined in huaweicloud sdk

        :param id: 资源ID标识符。
        :type id: str
        :param project_id: 实例所属项目ID。
        :type project_id: str
        :param local_region_id: 域间实例本端的RegionID。
        :type local_region_id: str
        :param remote_region_id: 域间实例对端的RegionID。
        :type remote_region_id: str
        """
        
        

        self._id = None
        self._project_id = None
        self._local_region_id = None
        self._remote_region_id = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        if local_region_id is not None:
            self.local_region_id = local_region_id
        if remote_region_id is not None:
            self.remote_region_id = remote_region_id

    @property
    def id(self):
        """Gets the id of this InterRegion.

        资源ID标识符。

        :return: The id of this InterRegion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InterRegion.

        资源ID标识符。

        :param id: The id of this InterRegion.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this InterRegion.

        实例所属项目ID。

        :return: The project_id of this InterRegion.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this InterRegion.

        实例所属项目ID。

        :param project_id: The project_id of this InterRegion.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def local_region_id(self):
        """Gets the local_region_id of this InterRegion.

        域间实例本端的RegionID。

        :return: The local_region_id of this InterRegion.
        :rtype: str
        """
        return self._local_region_id

    @local_region_id.setter
    def local_region_id(self, local_region_id):
        """Sets the local_region_id of this InterRegion.

        域间实例本端的RegionID。

        :param local_region_id: The local_region_id of this InterRegion.
        :type local_region_id: str
        """
        self._local_region_id = local_region_id

    @property
    def remote_region_id(self):
        """Gets the remote_region_id of this InterRegion.

        域间实例对端的RegionID。

        :return: The remote_region_id of this InterRegion.
        :rtype: str
        """
        return self._remote_region_id

    @remote_region_id.setter
    def remote_region_id(self, remote_region_id):
        """Sets the remote_region_id of this InterRegion.

        域间实例对端的RegionID。

        :param remote_region_id: The remote_region_id of this InterRegion.
        :type remote_region_id: str
        """
        self._remote_region_id = remote_region_id

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
        if not isinstance(other, InterRegion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
