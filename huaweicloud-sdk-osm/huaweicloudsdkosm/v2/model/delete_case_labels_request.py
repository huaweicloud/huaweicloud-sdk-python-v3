# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteCaseLabelsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_id': 'str',
        'label_ids': 'list[int]',
        'x_site': 'int',
        'x_language': 'str',
        'x_time_zone': 'str'
    }

    attribute_map = {
        'case_id': 'case_id',
        'label_ids': 'label_ids',
        'x_site': 'X-Site',
        'x_language': 'X-Language',
        'x_time_zone': 'X-Time-Zone'
    }

    def __init__(self, case_id=None, label_ids=None, x_site=None, x_language=None, x_time_zone=None):
        r"""DeleteCaseLabelsRequest

        The model defined in huaweicloud sdk

        :param case_id: 工单id
        :type case_id: str
        :param label_ids: 要取消关联的标签id，最多5个
        :type label_ids: list[int]
        :param x_site: 对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。
        :type x_site: int
        :param x_language: 语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。
        :type x_language: str
        :param x_time_zone: 环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。
        :type x_time_zone: str
        """
        
        

        self._case_id = None
        self._label_ids = None
        self._x_site = None
        self._x_language = None
        self._x_time_zone = None
        self.discriminator = None

        self.case_id = case_id
        self.label_ids = label_ids
        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        if x_time_zone is not None:
            self.x_time_zone = x_time_zone

    @property
    def case_id(self):
        r"""Gets the case_id of this DeleteCaseLabelsRequest.

        工单id

        :return: The case_id of this DeleteCaseLabelsRequest.
        :rtype: str
        """
        return self._case_id

    @case_id.setter
    def case_id(self, case_id):
        r"""Sets the case_id of this DeleteCaseLabelsRequest.

        工单id

        :param case_id: The case_id of this DeleteCaseLabelsRequest.
        :type case_id: str
        """
        self._case_id = case_id

    @property
    def label_ids(self):
        r"""Gets the label_ids of this DeleteCaseLabelsRequest.

        要取消关联的标签id，最多5个

        :return: The label_ids of this DeleteCaseLabelsRequest.
        :rtype: list[int]
        """
        return self._label_ids

    @label_ids.setter
    def label_ids(self, label_ids):
        r"""Sets the label_ids of this DeleteCaseLabelsRequest.

        要取消关联的标签id，最多5个

        :param label_ids: The label_ids of this DeleteCaseLabelsRequest.
        :type label_ids: list[int]
        """
        self._label_ids = label_ids

    @property
    def x_site(self):
        r"""Gets the x_site of this DeleteCaseLabelsRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :return: The x_site of this DeleteCaseLabelsRequest.
        :rtype: int
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        r"""Sets the x_site of this DeleteCaseLabelsRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :param x_site: The x_site of this DeleteCaseLabelsRequest.
        :type x_site: int
        """
        self._x_site = x_site

    @property
    def x_language(self):
        r"""Gets the x_language of this DeleteCaseLabelsRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :return: The x_language of this DeleteCaseLabelsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this DeleteCaseLabelsRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :param x_language: The x_language of this DeleteCaseLabelsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_time_zone(self):
        r"""Gets the x_time_zone of this DeleteCaseLabelsRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :return: The x_time_zone of this DeleteCaseLabelsRequest.
        :rtype: str
        """
        return self._x_time_zone

    @x_time_zone.setter
    def x_time_zone(self, x_time_zone):
        r"""Sets the x_time_zone of this DeleteCaseLabelsRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :param x_time_zone: The x_time_zone of this DeleteCaseLabelsRequest.
        :type x_time_zone: str
        """
        self._x_time_zone = x_time_zone

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
        if not isinstance(other, DeleteCaseLabelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
