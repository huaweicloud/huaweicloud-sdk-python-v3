# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLayoutResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'return_code': 'int',
        'return_desc': 'str',
        'pic_layouts': 'list[RestPicLayout]'
    }

    attribute_map = {
        'return_code': 'returnCode',
        'return_desc': 'returnDesc',
        'pic_layouts': 'picLayouts'
    }

    def __init__(self, return_code=None, return_desc=None, pic_layouts=None):
        """ShowLayoutResponse

        The model defined in huaweicloud sdk

        :param return_code: 结果码。 * 0：成功 * 非0：失败 
        :type return_code: int
        :param return_desc: 结果描述。 * Success：成功 * 其他：失败原因 
        :type return_desc: str
        :param pic_layouts: 多画面布局。
        :type pic_layouts: list[:class:`huaweicloudsdkmeeting.v1.RestPicLayout`]
        """
        
        super(ShowLayoutResponse, self).__init__()

        self._return_code = None
        self._return_desc = None
        self._pic_layouts = None
        self.discriminator = None

        if return_code is not None:
            self.return_code = return_code
        if return_desc is not None:
            self.return_desc = return_desc
        if pic_layouts is not None:
            self.pic_layouts = pic_layouts

    @property
    def return_code(self):
        """Gets the return_code of this ShowLayoutResponse.

        结果码。 * 0：成功 * 非0：失败 

        :return: The return_code of this ShowLayoutResponse.
        :rtype: int
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """Sets the return_code of this ShowLayoutResponse.

        结果码。 * 0：成功 * 非0：失败 

        :param return_code: The return_code of this ShowLayoutResponse.
        :type return_code: int
        """
        self._return_code = return_code

    @property
    def return_desc(self):
        """Gets the return_desc of this ShowLayoutResponse.

        结果描述。 * Success：成功 * 其他：失败原因 

        :return: The return_desc of this ShowLayoutResponse.
        :rtype: str
        """
        return self._return_desc

    @return_desc.setter
    def return_desc(self, return_desc):
        """Sets the return_desc of this ShowLayoutResponse.

        结果描述。 * Success：成功 * 其他：失败原因 

        :param return_desc: The return_desc of this ShowLayoutResponse.
        :type return_desc: str
        """
        self._return_desc = return_desc

    @property
    def pic_layouts(self):
        """Gets the pic_layouts of this ShowLayoutResponse.

        多画面布局。

        :return: The pic_layouts of this ShowLayoutResponse.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.RestPicLayout`]
        """
        return self._pic_layouts

    @pic_layouts.setter
    def pic_layouts(self, pic_layouts):
        """Sets the pic_layouts of this ShowLayoutResponse.

        多画面布局。

        :param pic_layouts: The pic_layouts of this ShowLayoutResponse.
        :type pic_layouts: list[:class:`huaweicloudsdkmeeting.v1.RestPicLayout`]
        """
        self._pic_layouts = pic_layouts

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
        if not isinstance(other, ShowLayoutResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
