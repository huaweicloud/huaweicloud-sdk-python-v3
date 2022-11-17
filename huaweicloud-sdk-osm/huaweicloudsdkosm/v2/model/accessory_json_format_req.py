# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessoryJsonFormatReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'accessory_name': 'str',
        'accessory_from': 'str',
        'upload_type': 'int',
        'accessory_data': 'str'
    }

    attribute_map = {
        'accessory_name': 'accessory_name',
        'accessory_from': 'accessory_from',
        'upload_type': 'upload_type',
        'accessory_data': 'accessory_data'
    }

    def __init__(self, accessory_name=None, accessory_from=None, upload_type=None, accessory_data=None):
        """AccessoryJsonFormatReq

        The model defined in huaweicloud sdk

        :param accessory_name: 文件名称
        :type accessory_name: str
        :param accessory_from: 文件来源
        :type accessory_from: str
        :param upload_type: 上传类型
        :type upload_type: int
        :param accessory_data: 文件内容，Base64格式
        :type accessory_data: str
        """
        
        

        self._accessory_name = None
        self._accessory_from = None
        self._upload_type = None
        self._accessory_data = None
        self.discriminator = None

        if accessory_name is not None:
            self.accessory_name = accessory_name
        if accessory_from is not None:
            self.accessory_from = accessory_from
        if upload_type is not None:
            self.upload_type = upload_type
        self.accessory_data = accessory_data

    @property
    def accessory_name(self):
        """Gets the accessory_name of this AccessoryJsonFormatReq.

        文件名称

        :return: The accessory_name of this AccessoryJsonFormatReq.
        :rtype: str
        """
        return self._accessory_name

    @accessory_name.setter
    def accessory_name(self, accessory_name):
        """Sets the accessory_name of this AccessoryJsonFormatReq.

        文件名称

        :param accessory_name: The accessory_name of this AccessoryJsonFormatReq.
        :type accessory_name: str
        """
        self._accessory_name = accessory_name

    @property
    def accessory_from(self):
        """Gets the accessory_from of this AccessoryJsonFormatReq.

        文件来源

        :return: The accessory_from of this AccessoryJsonFormatReq.
        :rtype: str
        """
        return self._accessory_from

    @accessory_from.setter
    def accessory_from(self, accessory_from):
        """Sets the accessory_from of this AccessoryJsonFormatReq.

        文件来源

        :param accessory_from: The accessory_from of this AccessoryJsonFormatReq.
        :type accessory_from: str
        """
        self._accessory_from = accessory_from

    @property
    def upload_type(self):
        """Gets the upload_type of this AccessoryJsonFormatReq.

        上传类型

        :return: The upload_type of this AccessoryJsonFormatReq.
        :rtype: int
        """
        return self._upload_type

    @upload_type.setter
    def upload_type(self, upload_type):
        """Sets the upload_type of this AccessoryJsonFormatReq.

        上传类型

        :param upload_type: The upload_type of this AccessoryJsonFormatReq.
        :type upload_type: int
        """
        self._upload_type = upload_type

    @property
    def accessory_data(self):
        """Gets the accessory_data of this AccessoryJsonFormatReq.

        文件内容，Base64格式

        :return: The accessory_data of this AccessoryJsonFormatReq.
        :rtype: str
        """
        return self._accessory_data

    @accessory_data.setter
    def accessory_data(self, accessory_data):
        """Sets the accessory_data of this AccessoryJsonFormatReq.

        文件内容，Base64格式

        :param accessory_data: The accessory_data of this AccessoryJsonFormatReq.
        :type accessory_data: str
        """
        self._accessory_data = accessory_data

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
        if not isinstance(other, AccessoryJsonFormatReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
