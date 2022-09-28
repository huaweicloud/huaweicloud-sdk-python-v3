# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLabelPageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'label_pages': 'list[LabelPageListDto]',
        'count': 'int'
    }

    attribute_map = {
        'label_pages': 'label_pages',
        'count': 'count'
    }

    def __init__(self, label_pages=None, count=None):
        """ListLabelPageResponse

        The model defined in huaweicloud sdk

        :param label_pages: 标签页面列表
        :type label_pages: list[:class:`huaweicloudsdkeihealth.v1.LabelPageListDto`]
        :param count: 标签页面总条数
        :type count: int
        """
        
        super(ListLabelPageResponse, self).__init__()

        self._label_pages = None
        self._count = None
        self.discriminator = None

        if label_pages is not None:
            self.label_pages = label_pages
        if count is not None:
            self.count = count

    @property
    def label_pages(self):
        """Gets the label_pages of this ListLabelPageResponse.

        标签页面列表

        :return: The label_pages of this ListLabelPageResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.LabelPageListDto`]
        """
        return self._label_pages

    @label_pages.setter
    def label_pages(self, label_pages):
        """Sets the label_pages of this ListLabelPageResponse.

        标签页面列表

        :param label_pages: The label_pages of this ListLabelPageResponse.
        :type label_pages: list[:class:`huaweicloudsdkeihealth.v1.LabelPageListDto`]
        """
        self._label_pages = label_pages

    @property
    def count(self):
        """Gets the count of this ListLabelPageResponse.

        标签页面总条数

        :return: The count of this ListLabelPageResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListLabelPageResponse.

        标签页面总条数

        :param count: The count of this ListLabelPageResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListLabelPageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
