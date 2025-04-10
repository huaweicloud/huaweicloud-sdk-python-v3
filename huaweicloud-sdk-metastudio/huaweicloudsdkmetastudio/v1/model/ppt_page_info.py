# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PPTPageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_no': 'int',
        'file_id': 'str',
        'page_content': 'str'
    }

    attribute_map = {
        'page_no': 'page_no',
        'file_id': 'file_id',
        'page_content': 'page_content'
    }

    def __init__(self, page_no=None, file_id=None, page_content=None):
        r"""PPTPageInfo

        The model defined in huaweicloud sdk

        :param page_no: **参数解释**： 页面编号。 **约束限制**： 不涉及
        :type page_no: int
        :param file_id: **参数解释**： 页面对应图片文件ID。 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及
        :type file_id: str
        :param page_content: **参数解释**： 页面对应图片文件ID **约束限制**： 不涉及 **取值范围**： 字符长度0-2048位 **默认取值**： 不涉及。
        :type page_content: str
        """
        
        

        self._page_no = None
        self._file_id = None
        self._page_content = None
        self.discriminator = None

        if page_no is not None:
            self.page_no = page_no
        if file_id is not None:
            self.file_id = file_id
        if page_content is not None:
            self.page_content = page_content

    @property
    def page_no(self):
        r"""Gets the page_no of this PPTPageInfo.

        **参数解释**： 页面编号。 **约束限制**： 不涉及

        :return: The page_no of this PPTPageInfo.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this PPTPageInfo.

        **参数解释**： 页面编号。 **约束限制**： 不涉及

        :param page_no: The page_no of this PPTPageInfo.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def file_id(self):
        r"""Gets the file_id of this PPTPageInfo.

        **参数解释**： 页面对应图片文件ID。 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及

        :return: The file_id of this PPTPageInfo.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        r"""Sets the file_id of this PPTPageInfo.

        **参数解释**： 页面对应图片文件ID。 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及

        :param file_id: The file_id of this PPTPageInfo.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def page_content(self):
        r"""Gets the page_content of this PPTPageInfo.

        **参数解释**： 页面对应图片文件ID **约束限制**： 不涉及 **取值范围**： 字符长度0-2048位 **默认取值**： 不涉及。

        :return: The page_content of this PPTPageInfo.
        :rtype: str
        """
        return self._page_content

    @page_content.setter
    def page_content(self, page_content):
        r"""Sets the page_content of this PPTPageInfo.

        **参数解释**： 页面对应图片文件ID **约束限制**： 不涉及 **取值范围**： 字符长度0-2048位 **默认取值**： 不涉及。

        :param page_content: The page_content of this PPTPageInfo.
        :type page_content: str
        """
        self._page_content = page_content

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
        if not isinstance(other, PPTPageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
