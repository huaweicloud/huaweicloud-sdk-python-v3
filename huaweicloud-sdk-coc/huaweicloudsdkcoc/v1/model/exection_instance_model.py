# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExectionInstanceModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'target_instance': 'ResourceInstance',
        'gmt_created': 'int',
        'gmt_finished': 'int',
        'execute_costs': 'int',
        'status': 'str',
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'target_instance': 'target_instance',
        'gmt_created': 'gmt_created',
        'gmt_finished': 'gmt_finished',
        'execute_costs': 'execute_costs',
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, id=None, target_instance=None, gmt_created=None, gmt_finished=None, execute_costs=None, status=None, message=None):
        r"""ExectionInstanceModel

        The model defined in huaweicloud sdk

        :param id: 主键id
        :type id: int
        :param target_instance: 
        :type target_instance: :class:`huaweicloudsdkcoc.v1.ResourceInstance`
        :param gmt_created: 创建时间
        :type gmt_created: int
        :param gmt_finished: 完成时间
        :type gmt_finished: int
        :param execute_costs: 耗时时间，单位:秒
        :type execute_costs: int
        :param status: 实例执行状态
        :type status: str
        :param message: 实例执行日志
        :type message: str
        """
        
        

        self._id = None
        self._target_instance = None
        self._gmt_created = None
        self._gmt_finished = None
        self._execute_costs = None
        self._status = None
        self._message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if target_instance is not None:
            self.target_instance = target_instance
        if gmt_created is not None:
            self.gmt_created = gmt_created
        if gmt_finished is not None:
            self.gmt_finished = gmt_finished
        if execute_costs is not None:
            self.execute_costs = execute_costs
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message

    @property
    def id(self):
        r"""Gets the id of this ExectionInstanceModel.

        主键id

        :return: The id of this ExectionInstanceModel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ExectionInstanceModel.

        主键id

        :param id: The id of this ExectionInstanceModel.
        :type id: int
        """
        self._id = id

    @property
    def target_instance(self):
        r"""Gets the target_instance of this ExectionInstanceModel.

        :return: The target_instance of this ExectionInstanceModel.
        :rtype: :class:`huaweicloudsdkcoc.v1.ResourceInstance`
        """
        return self._target_instance

    @target_instance.setter
    def target_instance(self, target_instance):
        r"""Sets the target_instance of this ExectionInstanceModel.

        :param target_instance: The target_instance of this ExectionInstanceModel.
        :type target_instance: :class:`huaweicloudsdkcoc.v1.ResourceInstance`
        """
        self._target_instance = target_instance

    @property
    def gmt_created(self):
        r"""Gets the gmt_created of this ExectionInstanceModel.

        创建时间

        :return: The gmt_created of this ExectionInstanceModel.
        :rtype: int
        """
        return self._gmt_created

    @gmt_created.setter
    def gmt_created(self, gmt_created):
        r"""Sets the gmt_created of this ExectionInstanceModel.

        创建时间

        :param gmt_created: The gmt_created of this ExectionInstanceModel.
        :type gmt_created: int
        """
        self._gmt_created = gmt_created

    @property
    def gmt_finished(self):
        r"""Gets the gmt_finished of this ExectionInstanceModel.

        完成时间

        :return: The gmt_finished of this ExectionInstanceModel.
        :rtype: int
        """
        return self._gmt_finished

    @gmt_finished.setter
    def gmt_finished(self, gmt_finished):
        r"""Sets the gmt_finished of this ExectionInstanceModel.

        完成时间

        :param gmt_finished: The gmt_finished of this ExectionInstanceModel.
        :type gmt_finished: int
        """
        self._gmt_finished = gmt_finished

    @property
    def execute_costs(self):
        r"""Gets the execute_costs of this ExectionInstanceModel.

        耗时时间，单位:秒

        :return: The execute_costs of this ExectionInstanceModel.
        :rtype: int
        """
        return self._execute_costs

    @execute_costs.setter
    def execute_costs(self, execute_costs):
        r"""Sets the execute_costs of this ExectionInstanceModel.

        耗时时间，单位:秒

        :param execute_costs: The execute_costs of this ExectionInstanceModel.
        :type execute_costs: int
        """
        self._execute_costs = execute_costs

    @property
    def status(self):
        r"""Gets the status of this ExectionInstanceModel.

        实例执行状态

        :return: The status of this ExectionInstanceModel.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExectionInstanceModel.

        实例执行状态

        :param status: The status of this ExectionInstanceModel.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this ExectionInstanceModel.

        实例执行日志

        :return: The message of this ExectionInstanceModel.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ExectionInstanceModel.

        实例执行日志

        :param message: The message of this ExectionInstanceModel.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, ExectionInstanceModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
