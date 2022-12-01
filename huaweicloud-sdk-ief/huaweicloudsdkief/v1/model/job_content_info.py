# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobContentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_type': 'str',
        'targets': 'list[Target]',
        'task_data': 'str'
    }

    attribute_map = {
        'target_type': 'target_type',
        'targets': 'targets',
        'task_data': 'task_data'
    }

    def __init__(self, target_type=None, targets=None, task_data=None):
        """JobContentInfo

        The model defined in huaweicloud sdk

        :param target_type: 批量作业对象类型，支持如下选项： - node：边缘节点 - node_group：边缘节点组 - deployment：边缘应用
        :type target_type: str
        :param targets: 批量作业对象详情
        :type targets: list[:class:`huaweicloudsdkief.v1.Target`]
        :param task_data: 批量作业内容，仅在批量应用部署和批量应用升级时需要填写，填入的内容为：使用json结构体编写的创建应用部署接口请求体deployment参数，并将其转换为字符串
        :type task_data: str
        """
        
        

        self._target_type = None
        self._targets = None
        self._task_data = None
        self.discriminator = None

        if target_type is not None:
            self.target_type = target_type
        if targets is not None:
            self.targets = targets
        if task_data is not None:
            self.task_data = task_data

    @property
    def target_type(self):
        """Gets the target_type of this JobContentInfo.

        批量作业对象类型，支持如下选项： - node：边缘节点 - node_group：边缘节点组 - deployment：边缘应用

        :return: The target_type of this JobContentInfo.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this JobContentInfo.

        批量作业对象类型，支持如下选项： - node：边缘节点 - node_group：边缘节点组 - deployment：边缘应用

        :param target_type: The target_type of this JobContentInfo.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def targets(self):
        """Gets the targets of this JobContentInfo.

        批量作业对象详情

        :return: The targets of this JobContentInfo.
        :rtype: list[:class:`huaweicloudsdkief.v1.Target`]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this JobContentInfo.

        批量作业对象详情

        :param targets: The targets of this JobContentInfo.
        :type targets: list[:class:`huaweicloudsdkief.v1.Target`]
        """
        self._targets = targets

    @property
    def task_data(self):
        """Gets the task_data of this JobContentInfo.

        批量作业内容，仅在批量应用部署和批量应用升级时需要填写，填入的内容为：使用json结构体编写的创建应用部署接口请求体deployment参数，并将其转换为字符串

        :return: The task_data of this JobContentInfo.
        :rtype: str
        """
        return self._task_data

    @task_data.setter
    def task_data(self, task_data):
        """Sets the task_data of this JobContentInfo.

        批量作业内容，仅在批量应用部署和批量应用升级时需要填写，填入的内容为：使用json结构体编写的创建应用部署接口请求体deployment参数，并将其转换为字符串

        :param task_data: The task_data of this JobContentInfo.
        :type task_data: str
        """
        self._task_data = task_data

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
        if not isinstance(other, JobContentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
