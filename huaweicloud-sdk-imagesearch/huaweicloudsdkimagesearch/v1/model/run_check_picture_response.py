# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunCheckPictureResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exist': 'str'
    }

    attribute_map = {
        'exist': 'exist'
    }

    def __init__(self, exist=None):
        """RunCheckPictureResponse

        The model defined in huaweicloud sdk

        :param exist: 调用成功时表示调用结果。  调用失败时无此字段。  - true表示图像索引库中存在查询的图片。  - false表示图像索引库中不存在查询的图片。 
        :type exist: str
        """
        
        super(RunCheckPictureResponse, self).__init__()

        self._exist = None
        self.discriminator = None

        if exist is not None:
            self.exist = exist

    @property
    def exist(self):
        """Gets the exist of this RunCheckPictureResponse.

        调用成功时表示调用结果。  调用失败时无此字段。  - true表示图像索引库中存在查询的图片。  - false表示图像索引库中不存在查询的图片。 

        :return: The exist of this RunCheckPictureResponse.
        :rtype: str
        """
        return self._exist

    @exist.setter
    def exist(self, exist):
        """Sets the exist of this RunCheckPictureResponse.

        调用成功时表示调用结果。  调用失败时无此字段。  - true表示图像索引库中存在查询的图片。  - false表示图像索引库中不存在查询的图片。 

        :param exist: The exist of this RunCheckPictureResponse.
        :type exist: str
        """
        self._exist = exist

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
        if not isinstance(other, RunCheckPictureResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
