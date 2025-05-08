# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetScriptJobBatchRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch_index': 'int',
        'execute_uuid': 'str',
        'status': 'str',
        'limit': 'int',
        'marker': 'int',
        'x_language': 'str',
        'x_project_id': 'str',
        'x_user_profile': 'str'
    }

    attribute_map = {
        'batch_index': 'batch_index',
        'execute_uuid': 'execute_uuid',
        'status': 'status',
        'limit': 'limit',
        'marker': 'marker',
        'x_language': 'X-Language',
        'x_project_id': 'x-project-id',
        'x_user_profile': 'x-user-profile'
    }

    def __init__(self, batch_index=None, execute_uuid=None, status=None, limit=None, marker=None, x_language=None, x_project_id=None, x_user_profile=None):
        r"""GetScriptJobBatchRequest

        The model defined in huaweicloud sdk

        :param batch_index: 批次index
        :type batch_index: int
        :param execute_uuid: 脚本工单的执行Id，取自executeJobScript和ListJobScriptOrders返回体中
        :type execute_uuid: str
        :param status: 实例执行状态 READY：待执行 PROCESSING：执行中 ABNORMAL：异常 CANCELED：已取消 FINISHED：成功
        :type status: str
        :param limit: 分页参数：每页返回记录个数限制
        :type limit: int
        :param marker: 分页参数：上一页最后一个记录id
        :type marker: int
        :param x_language: 国际化标记，zh-cn表示中文，en-us或不传表示英文
        :type x_language: str
        :param x_project_id: 项目ID，一个项目对应一个region
        :type x_project_id: str
        :param x_user_profile: IAM5.0用户信息
        :type x_user_profile: str
        """
        
        

        self._batch_index = None
        self._execute_uuid = None
        self._status = None
        self._limit = None
        self._marker = None
        self._x_language = None
        self._x_project_id = None
        self._x_user_profile = None
        self.discriminator = None

        self.batch_index = batch_index
        self.execute_uuid = execute_uuid
        if status is not None:
            self.status = status
        self.limit = limit
        if marker is not None:
            self.marker = marker
        if x_language is not None:
            self.x_language = x_language
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if x_user_profile is not None:
            self.x_user_profile = x_user_profile

    @property
    def batch_index(self):
        r"""Gets the batch_index of this GetScriptJobBatchRequest.

        批次index

        :return: The batch_index of this GetScriptJobBatchRequest.
        :rtype: int
        """
        return self._batch_index

    @batch_index.setter
    def batch_index(self, batch_index):
        r"""Sets the batch_index of this GetScriptJobBatchRequest.

        批次index

        :param batch_index: The batch_index of this GetScriptJobBatchRequest.
        :type batch_index: int
        """
        self._batch_index = batch_index

    @property
    def execute_uuid(self):
        r"""Gets the execute_uuid of this GetScriptJobBatchRequest.

        脚本工单的执行Id，取自executeJobScript和ListJobScriptOrders返回体中

        :return: The execute_uuid of this GetScriptJobBatchRequest.
        :rtype: str
        """
        return self._execute_uuid

    @execute_uuid.setter
    def execute_uuid(self, execute_uuid):
        r"""Sets the execute_uuid of this GetScriptJobBatchRequest.

        脚本工单的执行Id，取自executeJobScript和ListJobScriptOrders返回体中

        :param execute_uuid: The execute_uuid of this GetScriptJobBatchRequest.
        :type execute_uuid: str
        """
        self._execute_uuid = execute_uuid

    @property
    def status(self):
        r"""Gets the status of this GetScriptJobBatchRequest.

        实例执行状态 READY：待执行 PROCESSING：执行中 ABNORMAL：异常 CANCELED：已取消 FINISHED：成功

        :return: The status of this GetScriptJobBatchRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GetScriptJobBatchRequest.

        实例执行状态 READY：待执行 PROCESSING：执行中 ABNORMAL：异常 CANCELED：已取消 FINISHED：成功

        :param status: The status of this GetScriptJobBatchRequest.
        :type status: str
        """
        self._status = status

    @property
    def limit(self):
        r"""Gets the limit of this GetScriptJobBatchRequest.

        分页参数：每页返回记录个数限制

        :return: The limit of this GetScriptJobBatchRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this GetScriptJobBatchRequest.

        分页参数：每页返回记录个数限制

        :param limit: The limit of this GetScriptJobBatchRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this GetScriptJobBatchRequest.

        分页参数：上一页最后一个记录id

        :return: The marker of this GetScriptJobBatchRequest.
        :rtype: int
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this GetScriptJobBatchRequest.

        分页参数：上一页最后一个记录id

        :param marker: The marker of this GetScriptJobBatchRequest.
        :type marker: int
        """
        self._marker = marker

    @property
    def x_language(self):
        r"""Gets the x_language of this GetScriptJobBatchRequest.

        国际化标记，zh-cn表示中文，en-us或不传表示英文

        :return: The x_language of this GetScriptJobBatchRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this GetScriptJobBatchRequest.

        国际化标记，zh-cn表示中文，en-us或不传表示英文

        :param x_language: The x_language of this GetScriptJobBatchRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this GetScriptJobBatchRequest.

        项目ID，一个项目对应一个region

        :return: The x_project_id of this GetScriptJobBatchRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this GetScriptJobBatchRequest.

        项目ID，一个项目对应一个region

        :param x_project_id: The x_project_id of this GetScriptJobBatchRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def x_user_profile(self):
        r"""Gets the x_user_profile of this GetScriptJobBatchRequest.

        IAM5.0用户信息

        :return: The x_user_profile of this GetScriptJobBatchRequest.
        :rtype: str
        """
        return self._x_user_profile

    @x_user_profile.setter
    def x_user_profile(self, x_user_profile):
        r"""Sets the x_user_profile of this GetScriptJobBatchRequest.

        IAM5.0用户信息

        :param x_user_profile: The x_user_profile of this GetScriptJobBatchRequest.
        :type x_user_profile: str
        """
        self._x_user_profile = x_user_profile

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
        if not isinstance(other, GetScriptJobBatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
