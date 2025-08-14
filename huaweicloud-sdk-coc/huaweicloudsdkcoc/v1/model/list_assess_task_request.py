# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssessTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'application_id': 'str',
        'assess_status_list': 'list[str]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'application_id': 'application_id',
        'assess_status_list': 'assess_status_list'
    }

    def __init__(self, offset=None, limit=None, application_id=None, assess_status_list=None):
        r"""ListAssessTaskRequest

        The model defined in huaweicloud sdk

        :param offset: 分页参数
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param application_id: 应用id
        :type application_id: str
        :param assess_status_list: 评估任务状态
        :type assess_status_list: list[str]
        """
        
        

        self._offset = None
        self._limit = None
        self._application_id = None
        self._assess_status_list = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        if application_id is not None:
            self.application_id = application_id
        if assess_status_list is not None:
            self.assess_status_list = assess_status_list

    @property
    def offset(self):
        r"""Gets the offset of this ListAssessTaskRequest.

        分页参数

        :return: The offset of this ListAssessTaskRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAssessTaskRequest.

        分页参数

        :param offset: The offset of this ListAssessTaskRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAssessTaskRequest.

        每页显示的条目数量

        :return: The limit of this ListAssessTaskRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAssessTaskRequest.

        每页显示的条目数量

        :param limit: The limit of this ListAssessTaskRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def application_id(self):
        r"""Gets the application_id of this ListAssessTaskRequest.

        应用id

        :return: The application_id of this ListAssessTaskRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ListAssessTaskRequest.

        应用id

        :param application_id: The application_id of this ListAssessTaskRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def assess_status_list(self):
        r"""Gets the assess_status_list of this ListAssessTaskRequest.

        评估任务状态

        :return: The assess_status_list of this ListAssessTaskRequest.
        :rtype: list[str]
        """
        return self._assess_status_list

    @assess_status_list.setter
    def assess_status_list(self, assess_status_list):
        r"""Sets the assess_status_list of this ListAssessTaskRequest.

        评估任务状态

        :param assess_status_list: The assess_status_list of this ListAssessTaskRequest.
        :type assess_status_list: list[str]
        """
        self._assess_status_list = assess_status_list

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
        if not isinstance(other, ListAssessTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
