# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionDetails:

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
        'links': 'str',
        'version': 'str',
        'status': 'str',
        'updated': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'version': 'version',
        'status': 'status',
        'updated': 'updated'
    }

    def __init__(self, id=None, links=None, version=None, status=None, updated=None):
        """VersionDetails

        The model defined in huaweicloud sdk

        :param id: 版本ID。
        :type id: str
        :param links: 版本详情的URL地址。
        :type links: str
        :param version: 该版本API的微版本信息。
        :type version: str
        :param status: 版本的状态。
        :type status: str
        :param updated: 版本更新时间。
        :type updated: str
        """
        
        

        self._id = None
        self._links = None
        self._version = None
        self._status = None
        self._updated = None
        self.discriminator = None

        self.id = id
        self.links = links
        self.version = version
        self.status = status
        self.updated = updated

    @property
    def id(self):
        """Gets the id of this VersionDetails.

        版本ID。

        :return: The id of this VersionDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VersionDetails.

        版本ID。

        :param id: The id of this VersionDetails.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this VersionDetails.

        版本详情的URL地址。

        :return: The links of this VersionDetails.
        :rtype: str
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VersionDetails.

        版本详情的URL地址。

        :param links: The links of this VersionDetails.
        :type links: str
        """
        self._links = links

    @property
    def version(self):
        """Gets the version of this VersionDetails.

        该版本API的微版本信息。

        :return: The version of this VersionDetails.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VersionDetails.

        该版本API的微版本信息。

        :param version: The version of this VersionDetails.
        :type version: str
        """
        self._version = version

    @property
    def status(self):
        """Gets the status of this VersionDetails.

        版本的状态。

        :return: The status of this VersionDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VersionDetails.

        版本的状态。

        :param status: The status of this VersionDetails.
        :type status: str
        """
        self._status = status

    @property
    def updated(self):
        """Gets the updated of this VersionDetails.

        版本更新时间。

        :return: The updated of this VersionDetails.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this VersionDetails.

        版本更新时间。

        :param updated: The updated of this VersionDetails.
        :type updated: str
        """
        self._updated = updated

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
        if not isinstance(other, VersionDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
