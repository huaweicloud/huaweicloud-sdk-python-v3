# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteObjectsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "Delete"

    sensitive_list = []

    openapi_types = {
        'quiet': 'bool',
        'encoding_type': 'str',
        'object': 'list[DeleteObject]'
    }

    attribute_map = {
        'quiet': 'Quiet',
        'encoding_type': 'EncodingType',
        'object': 'Object'
    }

    def __init__(self, quiet=None, encoding_type=None, object=None):
        """DeleteObjectsRequestBody

        The model defined in huaweicloud sdk

        :param quiet: 用于指定使用quiet模式，只返回删除失败的对象结果；如果有此字段，则必被置为True，如果为False则被系统忽略掉。 
        :type quiet: bool
        :param encoding_type: 用于指定待删除的对象Key和响应中的对象Key的编码类型。如果Key包含xml 1.0标准不支持的控制字符，可通过设置该元素指定对象Key的编码类型。 
        :type encoding_type: str
        :param object: 
        :type object: list[:class:`huaweicloudsdkobs.v1.DeleteObject`]
        """
        
        

        self._quiet = None
        self._encoding_type = None
        self._object = None
        self.discriminator = None

        if quiet is not None:
            self.quiet = quiet
        if encoding_type is not None:
            self.encoding_type = encoding_type
        if object is not None:
            self.object = object

    @property
    def quiet(self):
        """Gets the quiet of this DeleteObjectsRequestBody.

        用于指定使用quiet模式，只返回删除失败的对象结果；如果有此字段，则必被置为True，如果为False则被系统忽略掉。 

        :return: The quiet of this DeleteObjectsRequestBody.
        :rtype: bool
        """
        return self._quiet

    @quiet.setter
    def quiet(self, quiet):
        """Sets the quiet of this DeleteObjectsRequestBody.

        用于指定使用quiet模式，只返回删除失败的对象结果；如果有此字段，则必被置为True，如果为False则被系统忽略掉。 

        :param quiet: The quiet of this DeleteObjectsRequestBody.
        :type quiet: bool
        """
        self._quiet = quiet

    @property
    def encoding_type(self):
        """Gets the encoding_type of this DeleteObjectsRequestBody.

        用于指定待删除的对象Key和响应中的对象Key的编码类型。如果Key包含xml 1.0标准不支持的控制字符，可通过设置该元素指定对象Key的编码类型。 

        :return: The encoding_type of this DeleteObjectsRequestBody.
        :rtype: str
        """
        return self._encoding_type

    @encoding_type.setter
    def encoding_type(self, encoding_type):
        """Sets the encoding_type of this DeleteObjectsRequestBody.

        用于指定待删除的对象Key和响应中的对象Key的编码类型。如果Key包含xml 1.0标准不支持的控制字符，可通过设置该元素指定对象Key的编码类型。 

        :param encoding_type: The encoding_type of this DeleteObjectsRequestBody.
        :type encoding_type: str
        """
        self._encoding_type = encoding_type

    @property
    def object(self):
        """Gets the object of this DeleteObjectsRequestBody.

        :return: The object of this DeleteObjectsRequestBody.
        :rtype: list[:class:`huaweicloudsdkobs.v1.DeleteObject`]
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this DeleteObjectsRequestBody.

        :param object: The object of this DeleteObjectsRequestBody.
        :type object: list[:class:`huaweicloudsdkobs.v1.DeleteObject`]
        """
        self._object = object

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
        if not isinstance(other, DeleteObjectsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
