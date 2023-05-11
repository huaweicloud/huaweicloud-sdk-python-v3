# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatisticCommitRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'ref_name': 'str',
        'begin_date': 'str',
        'end_date': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'ref_name': 'ref_name',
        'begin_date': 'begin_date',
        'end_date': 'end_date'
    }

    def __init__(self, repository_id=None, ref_name=None, begin_date=None, end_date=None):
        """ShowStatisticCommitRequest

        The model defined in huaweicloud sdk

        :param repository_id: 仓库短id
        :type repository_id: int
        :param ref_name: 分支名称
        :type ref_name: str
        :param begin_date: 起始提交日期,格式为yyyy-MM-dd
        :type begin_date: str
        :param end_date: 终止提交日期,格式为yyyy-MM-dd（begin_date和end_date时间间隔不超过60天）
        :type end_date: str
        """
        
        

        self._repository_id = None
        self._ref_name = None
        self._begin_date = None
        self._end_date = None
        self.discriminator = None

        self.repository_id = repository_id
        self.ref_name = ref_name
        self.begin_date = begin_date
        self.end_date = end_date

    @property
    def repository_id(self):
        """Gets the repository_id of this ShowStatisticCommitRequest.

        仓库短id

        :return: The repository_id of this ShowStatisticCommitRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this ShowStatisticCommitRequest.

        仓库短id

        :param repository_id: The repository_id of this ShowStatisticCommitRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def ref_name(self):
        """Gets the ref_name of this ShowStatisticCommitRequest.

        分支名称

        :return: The ref_name of this ShowStatisticCommitRequest.
        :rtype: str
        """
        return self._ref_name

    @ref_name.setter
    def ref_name(self, ref_name):
        """Sets the ref_name of this ShowStatisticCommitRequest.

        分支名称

        :param ref_name: The ref_name of this ShowStatisticCommitRequest.
        :type ref_name: str
        """
        self._ref_name = ref_name

    @property
    def begin_date(self):
        """Gets the begin_date of this ShowStatisticCommitRequest.

        起始提交日期,格式为yyyy-MM-dd

        :return: The begin_date of this ShowStatisticCommitRequest.
        :rtype: str
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this ShowStatisticCommitRequest.

        起始提交日期,格式为yyyy-MM-dd

        :param begin_date: The begin_date of this ShowStatisticCommitRequest.
        :type begin_date: str
        """
        self._begin_date = begin_date

    @property
    def end_date(self):
        """Gets the end_date of this ShowStatisticCommitRequest.

        终止提交日期,格式为yyyy-MM-dd（begin_date和end_date时间间隔不超过60天）

        :return: The end_date of this ShowStatisticCommitRequest.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ShowStatisticCommitRequest.

        终止提交日期,格式为yyyy-MM-dd（begin_date和end_date时间间隔不超过60天）

        :param end_date: The end_date of this ShowStatisticCommitRequest.
        :type end_date: str
        """
        self._end_date = end_date

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
        if not isinstance(other, ShowStatisticCommitRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
