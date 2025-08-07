# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DistinctSharedPrincipal:

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
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, updated_at=None):
        r"""DistinctSharedPrincipal

        The model defined in huaweicloud sdk

        :param id: 资源共享实例的创建者或使用者的账号ID或URN。
        :type id: str
        :param updated_at: 最后一次更新资源共享实例的时间。
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this DistinctSharedPrincipal.

        资源共享实例的创建者或使用者的账号ID或URN。

        :return: The id of this DistinctSharedPrincipal.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DistinctSharedPrincipal.

        资源共享实例的创建者或使用者的账号ID或URN。

        :param id: The id of this DistinctSharedPrincipal.
        :type id: str
        """
        self._id = id

    @property
    def updated_at(self):
        r"""Gets the updated_at of this DistinctSharedPrincipal.

        最后一次更新资源共享实例的时间。

        :return: The updated_at of this DistinctSharedPrincipal.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this DistinctSharedPrincipal.

        最后一次更新资源共享实例的时间。

        :param updated_at: The updated_at of this DistinctSharedPrincipal.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, DistinctSharedPrincipal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
