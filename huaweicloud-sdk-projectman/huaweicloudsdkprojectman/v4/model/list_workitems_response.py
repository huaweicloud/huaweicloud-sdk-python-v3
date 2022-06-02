# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkitemsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'work_items': 'list[Workitems]',
        'total': 'int'
    }

    attribute_map = {
        'work_items': 'work_items',
        'total': 'total'
    }

    def __init__(self, work_items=None, total=None):
        """ListWorkitemsResponse

        The model defined in huaweicloud sdk

        :param work_items: 工作项
        :type work_items: list[:class:`huaweicloudsdkprojectman.v4.Workitems`]
        :param total: 总数
        :type total: int
        """
        
        super(ListWorkitemsResponse, self).__init__()

        self._work_items = None
        self._total = None
        self.discriminator = None

        if work_items is not None:
            self.work_items = work_items
        if total is not None:
            self.total = total

    @property
    def work_items(self):
        """Gets the work_items of this ListWorkitemsResponse.

        工作项

        :return: The work_items of this ListWorkitemsResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.Workitems`]
        """
        return self._work_items

    @work_items.setter
    def work_items(self, work_items):
        """Sets the work_items of this ListWorkitemsResponse.

        工作项

        :param work_items: The work_items of this ListWorkitemsResponse.
        :type work_items: list[:class:`huaweicloudsdkprojectman.v4.Workitems`]
        """
        self._work_items = work_items

    @property
    def total(self):
        """Gets the total of this ListWorkitemsResponse.

        总数

        :return: The total of this ListWorkitemsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListWorkitemsResponse.

        总数

        :param total: The total of this ListWorkitemsResponse.
        :type total: int
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
        if not isinstance(other, ListWorkitemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
