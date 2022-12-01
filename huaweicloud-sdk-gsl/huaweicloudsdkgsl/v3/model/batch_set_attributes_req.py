# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSetAttributesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_temp_id': 'int',
        'attributes': 'list[AttributeReq]'
    }

    attribute_map = {
        'file_temp_id': 'file_temp_id',
        'attributes': 'attributes'
    }

    def __init__(self, file_temp_id=None, attributes=None):
        """BatchSetAttributesReq

        The model defined in huaweicloud sdk

        :param file_temp_id: 临时文件ID，如果通过接口调用，此字段为空
        :type file_temp_id: int
        :param attributes: 自定义属性集合
        :type attributes: list[:class:`huaweicloudsdkgsl.v3.AttributeReq`]
        """
        
        

        self._file_temp_id = None
        self._attributes = None
        self.discriminator = None

        if file_temp_id is not None:
            self.file_temp_id = file_temp_id
        if attributes is not None:
            self.attributes = attributes

    @property
    def file_temp_id(self):
        """Gets the file_temp_id of this BatchSetAttributesReq.

        临时文件ID，如果通过接口调用，此字段为空

        :return: The file_temp_id of this BatchSetAttributesReq.
        :rtype: int
        """
        return self._file_temp_id

    @file_temp_id.setter
    def file_temp_id(self, file_temp_id):
        """Sets the file_temp_id of this BatchSetAttributesReq.

        临时文件ID，如果通过接口调用，此字段为空

        :param file_temp_id: The file_temp_id of this BatchSetAttributesReq.
        :type file_temp_id: int
        """
        self._file_temp_id = file_temp_id

    @property
    def attributes(self):
        """Gets the attributes of this BatchSetAttributesReq.

        自定义属性集合

        :return: The attributes of this BatchSetAttributesReq.
        :rtype: list[:class:`huaweicloudsdkgsl.v3.AttributeReq`]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this BatchSetAttributesReq.

        自定义属性集合

        :param attributes: The attributes of this BatchSetAttributesReq.
        :type attributes: list[:class:`huaweicloudsdkgsl.v3.AttributeReq`]
        """
        self._attributes = attributes

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
        if not isinstance(other, BatchSetAttributesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
