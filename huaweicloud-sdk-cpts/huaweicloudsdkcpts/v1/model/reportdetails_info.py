# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportdetailsInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'data': 'list[ReportdetailItemInfo]',
        'page_index': 'int',
        'page_size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'data': 'data',
        'page_index': 'pageIndex',
        'page_size': 'pageSize',
        'total': 'total'
    }

    def __init__(self, data=None, page_index=None, page_size=None, total=None):
        """ReportdetailsInfo - a model defined in huaweicloud sdk"""
        
        

        self._data = None
        self._page_index = None
        self._page_size = None
        self._total = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size
        if total is not None:
            self.total = total

    @property
    def data(self):
        """Gets the data of this ReportdetailsInfo.

        data

        :return: The data of this ReportdetailsInfo.
        :rtype: list[ReportdetailItemInfo]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ReportdetailsInfo.

        data

        :param data: The data of this ReportdetailsInfo.
        :type: list[ReportdetailItemInfo]
        """
        self._data = data

    @property
    def page_index(self):
        """Gets the page_index of this ReportdetailsInfo.

        pageIndex

        :return: The page_index of this ReportdetailsInfo.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this ReportdetailsInfo.

        pageIndex

        :param page_index: The page_index of this ReportdetailsInfo.
        :type: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        """Gets the page_size of this ReportdetailsInfo.

        pageSize

        :return: The page_size of this ReportdetailsInfo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ReportdetailsInfo.

        pageSize

        :param page_size: The page_size of this ReportdetailsInfo.
        :type: int
        """
        self._page_size = page_size

    @property
    def total(self):
        """Gets the total of this ReportdetailsInfo.

        total

        :return: The total of this ReportdetailsInfo.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ReportdetailsInfo.

        total

        :param total: The total of this ReportdetailsInfo.
        :type: int
        """
        self._total = total

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
        if not isinstance(other, ReportdetailsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
