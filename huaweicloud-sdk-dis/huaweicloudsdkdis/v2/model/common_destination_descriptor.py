# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommonDestinationDescriptor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'agency_name': 'str',
        'deliver_time_interval': 'int',
        'consumer_strategy': 'str'
    }

    attribute_map = {
        'task_name': 'task_name',
        'agency_name': 'agency_name',
        'deliver_time_interval': 'deliver_time_interval',
        'consumer_strategy': 'consumer_strategy'
    }

    def __init__(self, task_name=None, agency_name=None, deliver_time_interval=None, consumer_strategy=None):
        """CommonDestinationDescriptor

        The model defined in huaweicloud sdk

        :param task_name: 转储任务的名称。  任务名称由英文字母、数字、中划线和下划线组成。长度为1～64个字符。
        :type task_name: str
        :param agency_name: 在统一身份认证服务(IAM)中创建委托的名称，DIS需要获取IAM委托信息去访问您指定的资源。创建委托的参数设置如下： - 委托类型：云服务 - 云服务：DIS - 持续时间：永久 - “所属区域”为“全局服务”，“项目”为“对象存储服务”对应的“策略”包含“Tenant Administrator”。 如果已经创建过委托，可以使用IAM服务提供的查询委托列表接口，获取有效可用的委托名称。 取值范围：长度不超过64位，且不可配置为空。  如果有在Console控制台使用转储任务，会提示自动创建委托，自动创建的委托名称为：dis_admin_agency
        :type agency_name: str
        :param deliver_time_interval: 根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。  单位：秒
        :type deliver_time_interval: int
        :param consumer_strategy: 偏移量。  - LATEST：最大偏移量，即获取最新的数据。 - TRIM_HORIZON：最小偏移量，即读取最早的数据。
        :type consumer_strategy: str
        """
        
        

        self._task_name = None
        self._agency_name = None
        self._deliver_time_interval = None
        self._consumer_strategy = None
        self.discriminator = None

        self.task_name = task_name
        self.agency_name = agency_name
        self.deliver_time_interval = deliver_time_interval
        if consumer_strategy is not None:
            self.consumer_strategy = consumer_strategy

    @property
    def task_name(self):
        """Gets the task_name of this CommonDestinationDescriptor.

        转储任务的名称。  任务名称由英文字母、数字、中划线和下划线组成。长度为1～64个字符。

        :return: The task_name of this CommonDestinationDescriptor.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this CommonDestinationDescriptor.

        转储任务的名称。  任务名称由英文字母、数字、中划线和下划线组成。长度为1～64个字符。

        :param task_name: The task_name of this CommonDestinationDescriptor.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def agency_name(self):
        """Gets the agency_name of this CommonDestinationDescriptor.

        在统一身份认证服务(IAM)中创建委托的名称，DIS需要获取IAM委托信息去访问您指定的资源。创建委托的参数设置如下： - 委托类型：云服务 - 云服务：DIS - 持续时间：永久 - “所属区域”为“全局服务”，“项目”为“对象存储服务”对应的“策略”包含“Tenant Administrator”。 如果已经创建过委托，可以使用IAM服务提供的查询委托列表接口，获取有效可用的委托名称。 取值范围：长度不超过64位，且不可配置为空。  如果有在Console控制台使用转储任务，会提示自动创建委托，自动创建的委托名称为：dis_admin_agency

        :return: The agency_name of this CommonDestinationDescriptor.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        """Sets the agency_name of this CommonDestinationDescriptor.

        在统一身份认证服务(IAM)中创建委托的名称，DIS需要获取IAM委托信息去访问您指定的资源。创建委托的参数设置如下： - 委托类型：云服务 - 云服务：DIS - 持续时间：永久 - “所属区域”为“全局服务”，“项目”为“对象存储服务”对应的“策略”包含“Tenant Administrator”。 如果已经创建过委托，可以使用IAM服务提供的查询委托列表接口，获取有效可用的委托名称。 取值范围：长度不超过64位，且不可配置为空。  如果有在Console控制台使用转储任务，会提示自动创建委托，自动创建的委托名称为：dis_admin_agency

        :param agency_name: The agency_name of this CommonDestinationDescriptor.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def deliver_time_interval(self):
        """Gets the deliver_time_interval of this CommonDestinationDescriptor.

        根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。  单位：秒

        :return: The deliver_time_interval of this CommonDestinationDescriptor.
        :rtype: int
        """
        return self._deliver_time_interval

    @deliver_time_interval.setter
    def deliver_time_interval(self, deliver_time_interval):
        """Sets the deliver_time_interval of this CommonDestinationDescriptor.

        根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。  单位：秒

        :param deliver_time_interval: The deliver_time_interval of this CommonDestinationDescriptor.
        :type deliver_time_interval: int
        """
        self._deliver_time_interval = deliver_time_interval

    @property
    def consumer_strategy(self):
        """Gets the consumer_strategy of this CommonDestinationDescriptor.

        偏移量。  - LATEST：最大偏移量，即获取最新的数据。 - TRIM_HORIZON：最小偏移量，即读取最早的数据。

        :return: The consumer_strategy of this CommonDestinationDescriptor.
        :rtype: str
        """
        return self._consumer_strategy

    @consumer_strategy.setter
    def consumer_strategy(self, consumer_strategy):
        """Sets the consumer_strategy of this CommonDestinationDescriptor.

        偏移量。  - LATEST：最大偏移量，即获取最新的数据。 - TRIM_HORIZON：最小偏移量，即读取最早的数据。

        :param consumer_strategy: The consumer_strategy of this CommonDestinationDescriptor.
        :type consumer_strategy: str
        """
        self._consumer_strategy = consumer_strategy

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
        if not isinstance(other, CommonDestinationDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
