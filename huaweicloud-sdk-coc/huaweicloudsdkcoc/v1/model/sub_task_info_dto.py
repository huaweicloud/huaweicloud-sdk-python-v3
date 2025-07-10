# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubTaskInfoDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_task_type': 'str',
        'sub_associated_task_id': 'str',
        'sub_associated_task_name': 'str',
        'sub_associated_task_type': 'str'
    }

    attribute_map = {
        'sub_task_type': 'sub_task_type',
        'sub_associated_task_id': 'sub_associated_task_id',
        'sub_associated_task_name': 'sub_associated_task_name',
        'sub_associated_task_type': 'sub_associated_task_type'
    }

    def __init__(self, sub_task_type=None, sub_associated_task_id=None, sub_associated_task_name=None, sub_associated_task_type=None):
        r"""SubTaskInfoDTO

        The model defined in huaweicloud sdk

        :param sub_task_type: 子任务类型
        :type sub_task_type: str
        :param sub_associated_task_id: 作业、脚本的id
        :type sub_associated_task_id: str
        :param sub_associated_task_name: 作业、脚本的名称
        :type sub_associated_task_name: str
        :param sub_associated_task_type: 作业、脚本的分类：自定义、公共
        :type sub_associated_task_type: str
        """
        
        

        self._sub_task_type = None
        self._sub_associated_task_id = None
        self._sub_associated_task_name = None
        self._sub_associated_task_type = None
        self.discriminator = None

        if sub_task_type is not None:
            self.sub_task_type = sub_task_type
        if sub_associated_task_id is not None:
            self.sub_associated_task_id = sub_associated_task_id
        if sub_associated_task_name is not None:
            self.sub_associated_task_name = sub_associated_task_name
        if sub_associated_task_type is not None:
            self.sub_associated_task_type = sub_associated_task_type

    @property
    def sub_task_type(self):
        r"""Gets the sub_task_type of this SubTaskInfoDTO.

        子任务类型

        :return: The sub_task_type of this SubTaskInfoDTO.
        :rtype: str
        """
        return self._sub_task_type

    @sub_task_type.setter
    def sub_task_type(self, sub_task_type):
        r"""Sets the sub_task_type of this SubTaskInfoDTO.

        子任务类型

        :param sub_task_type: The sub_task_type of this SubTaskInfoDTO.
        :type sub_task_type: str
        """
        self._sub_task_type = sub_task_type

    @property
    def sub_associated_task_id(self):
        r"""Gets the sub_associated_task_id of this SubTaskInfoDTO.

        作业、脚本的id

        :return: The sub_associated_task_id of this SubTaskInfoDTO.
        :rtype: str
        """
        return self._sub_associated_task_id

    @sub_associated_task_id.setter
    def sub_associated_task_id(self, sub_associated_task_id):
        r"""Sets the sub_associated_task_id of this SubTaskInfoDTO.

        作业、脚本的id

        :param sub_associated_task_id: The sub_associated_task_id of this SubTaskInfoDTO.
        :type sub_associated_task_id: str
        """
        self._sub_associated_task_id = sub_associated_task_id

    @property
    def sub_associated_task_name(self):
        r"""Gets the sub_associated_task_name of this SubTaskInfoDTO.

        作业、脚本的名称

        :return: The sub_associated_task_name of this SubTaskInfoDTO.
        :rtype: str
        """
        return self._sub_associated_task_name

    @sub_associated_task_name.setter
    def sub_associated_task_name(self, sub_associated_task_name):
        r"""Sets the sub_associated_task_name of this SubTaskInfoDTO.

        作业、脚本的名称

        :param sub_associated_task_name: The sub_associated_task_name of this SubTaskInfoDTO.
        :type sub_associated_task_name: str
        """
        self._sub_associated_task_name = sub_associated_task_name

    @property
    def sub_associated_task_type(self):
        r"""Gets the sub_associated_task_type of this SubTaskInfoDTO.

        作业、脚本的分类：自定义、公共

        :return: The sub_associated_task_type of this SubTaskInfoDTO.
        :rtype: str
        """
        return self._sub_associated_task_type

    @sub_associated_task_type.setter
    def sub_associated_task_type(self, sub_associated_task_type):
        r"""Sets the sub_associated_task_type of this SubTaskInfoDTO.

        作业、脚本的分类：自定义、公共

        :param sub_associated_task_type: The sub_associated_task_type of this SubTaskInfoDTO.
        :type sub_associated_task_type: str
        """
        self._sub_associated_task_type = sub_associated_task_type

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
        if not isinstance(other, SubTaskInfoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
