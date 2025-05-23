# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAimSendReportsMode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_list': 'list[AimSendReport]',
        'page_info': 'Page'
    }

    attribute_map = {
        'data_list': 'data_list',
        'page_info': 'page_info'
    }

    def __init__(self, data_list=None, page_info=None):
        r"""ListAimSendReportsMode

        The model defined in huaweicloud sdk

        :param data_list: 数据列表。
        :type data_list: list[:class:`huaweicloudsdkkoomessage.v1.AimSendReport`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        
        

        self._data_list = None
        self._page_info = None
        self.discriminator = None

        if data_list is not None:
            self.data_list = data_list
        if page_info is not None:
            self.page_info = page_info

    @property
    def data_list(self):
        r"""Gets the data_list of this ListAimSendReportsMode.

        数据列表。

        :return: The data_list of this ListAimSendReportsMode.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.AimSendReport`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListAimSendReportsMode.

        数据列表。

        :param data_list: The data_list of this ListAimSendReportsMode.
        :type data_list: list[:class:`huaweicloudsdkkoomessage.v1.AimSendReport`]
        """
        self._data_list = data_list

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAimSendReportsMode.

        :return: The page_info of this ListAimSendReportsMode.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAimSendReportsMode.

        :param page_info: The page_info of this ListAimSendReportsMode.
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListAimSendReportsMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
