# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineConcurrencyMgmt:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipeline_id': 'str',
        'concurrency_number': 'int',
        'exceed_action': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'enable': 'bool'
    }

    attribute_map = {
        'pipeline_id': 'pipeline_id',
        'concurrency_number': 'concurrency_number',
        'exceed_action': 'exceed_action',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'enable': 'enable'
    }

    def __init__(self, pipeline_id=None, concurrency_number=None, exceed_action=None, create_time=None, update_time=None, enable=None):
        r"""PipelineConcurrencyMgmt

        The model defined in huaweicloud sdk

        :param pipeline_id: 流水线id
        :type pipeline_id: str
        :param concurrency_number: 并行数量
        :type concurrency_number: int
        :param exceed_action: 超出情况下策略
        :type exceed_action: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        :param enable: 是否有效
        :type enable: bool
        """
        
        

        self._pipeline_id = None
        self._concurrency_number = None
        self._exceed_action = None
        self._create_time = None
        self._update_time = None
        self._enable = None
        self.discriminator = None

        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if concurrency_number is not None:
            self.concurrency_number = concurrency_number
        if exceed_action is not None:
            self.exceed_action = exceed_action
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if enable is not None:
            self.enable = enable

    @property
    def pipeline_id(self):
        r"""Gets the pipeline_id of this PipelineConcurrencyMgmt.

        流水线id

        :return: The pipeline_id of this PipelineConcurrencyMgmt.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        r"""Sets the pipeline_id of this PipelineConcurrencyMgmt.

        流水线id

        :param pipeline_id: The pipeline_id of this PipelineConcurrencyMgmt.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def concurrency_number(self):
        r"""Gets the concurrency_number of this PipelineConcurrencyMgmt.

        并行数量

        :return: The concurrency_number of this PipelineConcurrencyMgmt.
        :rtype: int
        """
        return self._concurrency_number

    @concurrency_number.setter
    def concurrency_number(self, concurrency_number):
        r"""Sets the concurrency_number of this PipelineConcurrencyMgmt.

        并行数量

        :param concurrency_number: The concurrency_number of this PipelineConcurrencyMgmt.
        :type concurrency_number: int
        """
        self._concurrency_number = concurrency_number

    @property
    def exceed_action(self):
        r"""Gets the exceed_action of this PipelineConcurrencyMgmt.

        超出情况下策略

        :return: The exceed_action of this PipelineConcurrencyMgmt.
        :rtype: str
        """
        return self._exceed_action

    @exceed_action.setter
    def exceed_action(self, exceed_action):
        r"""Sets the exceed_action of this PipelineConcurrencyMgmt.

        超出情况下策略

        :param exceed_action: The exceed_action of this PipelineConcurrencyMgmt.
        :type exceed_action: str
        """
        self._exceed_action = exceed_action

    @property
    def create_time(self):
        r"""Gets the create_time of this PipelineConcurrencyMgmt.

        创建时间

        :return: The create_time of this PipelineConcurrencyMgmt.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PipelineConcurrencyMgmt.

        创建时间

        :param create_time: The create_time of this PipelineConcurrencyMgmt.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this PipelineConcurrencyMgmt.

        更新时间

        :return: The update_time of this PipelineConcurrencyMgmt.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this PipelineConcurrencyMgmt.

        更新时间

        :param update_time: The update_time of this PipelineConcurrencyMgmt.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def enable(self):
        r"""Gets the enable of this PipelineConcurrencyMgmt.

        是否有效

        :return: The enable of this PipelineConcurrencyMgmt.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this PipelineConcurrencyMgmt.

        是否有效

        :param enable: The enable of this PipelineConcurrencyMgmt.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, PipelineConcurrencyMgmt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
