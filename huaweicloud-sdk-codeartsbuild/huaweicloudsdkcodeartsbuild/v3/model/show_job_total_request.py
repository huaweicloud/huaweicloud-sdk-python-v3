# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobTotalRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'build_project_id': 'str',
        'from_date': 'str',
        'to_date': 'str'
    }

    attribute_map = {
        'build_project_id': 'build_project_id',
        'from_date': 'from_date',
        'to_date': 'to_date'
    }

    def __init__(self, build_project_id=None, from_date=None, to_date=None):
        r"""ShowJobTotalRequest

        The model defined in huaweicloud sdk

        :param build_project_id: 构建工程项目ID，36位数字、小写字母组合。
        :type build_project_id: str
        :param from_date: 区间开始时间，格式yyyy-MM-dd HH:mm:ss。
        :type from_date: str
        :param to_date: 区间结束时间，格式yyyy-MM-dd HH:mm:ss。
        :type to_date: str
        """
        
        

        self._build_project_id = None
        self._from_date = None
        self._to_date = None
        self.discriminator = None

        self.build_project_id = build_project_id
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date

    @property
    def build_project_id(self):
        r"""Gets the build_project_id of this ShowJobTotalRequest.

        构建工程项目ID，36位数字、小写字母组合。

        :return: The build_project_id of this ShowJobTotalRequest.
        :rtype: str
        """
        return self._build_project_id

    @build_project_id.setter
    def build_project_id(self, build_project_id):
        r"""Sets the build_project_id of this ShowJobTotalRequest.

        构建工程项目ID，36位数字、小写字母组合。

        :param build_project_id: The build_project_id of this ShowJobTotalRequest.
        :type build_project_id: str
        """
        self._build_project_id = build_project_id

    @property
    def from_date(self):
        r"""Gets the from_date of this ShowJobTotalRequest.

        区间开始时间，格式yyyy-MM-dd HH:mm:ss。

        :return: The from_date of this ShowJobTotalRequest.
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        r"""Sets the from_date of this ShowJobTotalRequest.

        区间开始时间，格式yyyy-MM-dd HH:mm:ss。

        :param from_date: The from_date of this ShowJobTotalRequest.
        :type from_date: str
        """
        self._from_date = from_date

    @property
    def to_date(self):
        r"""Gets the to_date of this ShowJobTotalRequest.

        区间结束时间，格式yyyy-MM-dd HH:mm:ss。

        :return: The to_date of this ShowJobTotalRequest.
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        r"""Sets the to_date of this ShowJobTotalRequest.

        区间结束时间，格式yyyy-MM-dd HH:mm:ss。

        :param to_date: The to_date of this ShowJobTotalRequest.
        :type to_date: str
        """
        self._to_date = to_date

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
        if not isinstance(other, ShowJobTotalRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
