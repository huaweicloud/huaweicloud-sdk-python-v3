# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListExecutionStepsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'execution_step_id_list': 'list[str]'
    }

    attribute_map = {
        'execution_id': 'execution_id',
        'limit': 'limit',
        'offset': 'offset',
        'execution_step_id_list': 'execution_step_id_list'
    }

    def __init__(self, execution_id=None, limit=None, offset=None, execution_step_id_list=None):
        r"""ListExecutionStepsRequest

        The model defined in huaweicloud sdk

        :param execution_id: 
        :type execution_id: str
        :param limit: 每页显示的条目数量
        :type limit: int
        :param offset: 从offset指定的下一条数据开始查询
        :type offset: int
        :param execution_step_id_list: 步骤id数组
        :type execution_step_id_list: list[str]
        """
        
        

        self._execution_id = None
        self._limit = None
        self._offset = None
        self._execution_step_id_list = None
        self.discriminator = None

        self.execution_id = execution_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if execution_step_id_list is not None:
            self.execution_step_id_list = execution_step_id_list

    @property
    def execution_id(self):
        r"""Gets the execution_id of this ListExecutionStepsRequest.

        :return: The execution_id of this ListExecutionStepsRequest.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this ListExecutionStepsRequest.

        :param execution_id: The execution_id of this ListExecutionStepsRequest.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def limit(self):
        r"""Gets the limit of this ListExecutionStepsRequest.

        每页显示的条目数量

        :return: The limit of this ListExecutionStepsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListExecutionStepsRequest.

        每页显示的条目数量

        :param limit: The limit of this ListExecutionStepsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListExecutionStepsRequest.

        从offset指定的下一条数据开始查询

        :return: The offset of this ListExecutionStepsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListExecutionStepsRequest.

        从offset指定的下一条数据开始查询

        :param offset: The offset of this ListExecutionStepsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def execution_step_id_list(self):
        r"""Gets the execution_step_id_list of this ListExecutionStepsRequest.

        步骤id数组

        :return: The execution_step_id_list of this ListExecutionStepsRequest.
        :rtype: list[str]
        """
        return self._execution_step_id_list

    @execution_step_id_list.setter
    def execution_step_id_list(self, execution_step_id_list):
        r"""Sets the execution_step_id_list of this ListExecutionStepsRequest.

        步骤id数组

        :param execution_step_id_list: The execution_step_id_list of this ListExecutionStepsRequest.
        :type execution_step_id_list: list[str]
        """
        self._execution_step_id_list = execution_step_id_list

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
        if not isinstance(other, ListExecutionStepsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
