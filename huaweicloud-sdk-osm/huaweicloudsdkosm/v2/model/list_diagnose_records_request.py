# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDiagnoseRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_size': 'int',
        'page_no': 'int',
        'type': 'int'
    }

    attribute_map = {
        'page_size': 'page_size',
        'page_no': 'page_no',
        'type': 'type'
    }

    def __init__(self, page_size=None, page_no=None, type=None):
        r"""ListDiagnoseRecordsRequest

        The model defined in huaweicloud sdk

        :param page_size: 单页大小
        :type page_size: int
        :param page_no: 页码
        :type page_no: int
        :param type: 任务类型，例如 ecs诊断任务 1，rds诊断任务 2
        :type type: int
        """
        
        

        self._page_size = None
        self._page_no = None
        self._type = None
        self.discriminator = None

        if page_size is not None:
            self.page_size = page_size
        if page_no is not None:
            self.page_no = page_no
        if type is not None:
            self.type = type

    @property
    def page_size(self):
        r"""Gets the page_size of this ListDiagnoseRecordsRequest.

        单页大小

        :return: The page_size of this ListDiagnoseRecordsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListDiagnoseRecordsRequest.

        单页大小

        :param page_size: The page_size of this ListDiagnoseRecordsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_no(self):
        r"""Gets the page_no of this ListDiagnoseRecordsRequest.

        页码

        :return: The page_no of this ListDiagnoseRecordsRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListDiagnoseRecordsRequest.

        页码

        :param page_no: The page_no of this ListDiagnoseRecordsRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def type(self):
        r"""Gets the type of this ListDiagnoseRecordsRequest.

        任务类型，例如 ecs诊断任务 1，rds诊断任务 2

        :return: The type of this ListDiagnoseRecordsRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListDiagnoseRecordsRequest.

        任务类型，例如 ecs诊断任务 1，rds诊断任务 2

        :param type: The type of this ListDiagnoseRecordsRequest.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, ListDiagnoseRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
