# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CmTagVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'tag_name': 'str',
        'status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'tag_name': 'tag_name',
        'status': 'status'
    }

    def __init__(self, id=None, tag_name=None, status=None):
        """CmTagVO

        The model defined in huaweicloud sdk

        :param id: 标签标识
        :type id: int
        :param tag_name: 标签名称
        :type tag_name: str
        :param status: 标签状态，0未使用，1使用中。
        :type status: int
        """
        
        

        self._id = None
        self._tag_name = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tag_name is not None:
            self.tag_name = tag_name
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this CmTagVO.

        标签标识

        :return: The id of this CmTagVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CmTagVO.

        标签标识

        :param id: The id of this CmTagVO.
        :type id: int
        """
        self._id = id

    @property
    def tag_name(self):
        """Gets the tag_name of this CmTagVO.

        标签名称

        :return: The tag_name of this CmTagVO.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this CmTagVO.

        标签名称

        :param tag_name: The tag_name of this CmTagVO.
        :type tag_name: str
        """
        self._tag_name = tag_name

    @property
    def status(self):
        """Gets the status of this CmTagVO.

        标签状态，0未使用，1使用中。

        :return: The status of this CmTagVO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CmTagVO.

        标签状态，0未使用，1使用中。

        :param status: The status of this CmTagVO.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, CmTagVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
