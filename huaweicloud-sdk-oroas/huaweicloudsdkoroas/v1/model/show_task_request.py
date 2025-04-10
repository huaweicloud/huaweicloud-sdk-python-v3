# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_apig_app_code': 'str',
        'service_group': 'str',
        'service_type': 'str',
        'task_id': 'str',
        'input_enable': 'bool'
    }

    attribute_map = {
        'x_apig_app_code': 'X-Apig-AppCode',
        'service_group': 'service_group',
        'service_type': 'service_type',
        'task_id': 'task_id',
        'input_enable': 'input_enable'
    }

    def __init__(self, x_apig_app_code=None, service_group=None, service_type=None, task_id=None, input_enable=None):
        r"""ShowTaskRequest

        The model defined in huaweicloud sdk

        :param x_apig_app_code: 用户凭证
        :type x_apig_app_code: str
        :param service_group: 服务类别，针对不同服务类场景，为用户提前填充对应值，用户侧不需单独赋值；当前仅支持 二维切割 2dcut ，便于后续扩展
        :type service_group: str
        :param service_type: 子服务类型，针对不同服务，为用户提前填充对应值，用户侧不需单独赋值；服装切割固定为 irregular-textile，雕刻机切割固定为 engraving-machine-cutting， 板材切割固定为 regular-plate
        :type service_type: str
        :param task_id: 任务id
        :type task_id: str
        :param input_enable: 是否返回输入信息，默认为false； 当前暂不支持该功能，后续扩展
        :type input_enable: bool
        """
        
        

        self._x_apig_app_code = None
        self._service_group = None
        self._service_type = None
        self._task_id = None
        self._input_enable = None
        self.discriminator = None

        self.x_apig_app_code = x_apig_app_code
        self.service_group = service_group
        self.service_type = service_type
        self.task_id = task_id
        if input_enable is not None:
            self.input_enable = input_enable

    @property
    def x_apig_app_code(self):
        r"""Gets the x_apig_app_code of this ShowTaskRequest.

        用户凭证

        :return: The x_apig_app_code of this ShowTaskRequest.
        :rtype: str
        """
        return self._x_apig_app_code

    @x_apig_app_code.setter
    def x_apig_app_code(self, x_apig_app_code):
        r"""Sets the x_apig_app_code of this ShowTaskRequest.

        用户凭证

        :param x_apig_app_code: The x_apig_app_code of this ShowTaskRequest.
        :type x_apig_app_code: str
        """
        self._x_apig_app_code = x_apig_app_code

    @property
    def service_group(self):
        r"""Gets the service_group of this ShowTaskRequest.

        服务类别，针对不同服务类场景，为用户提前填充对应值，用户侧不需单独赋值；当前仅支持 二维切割 2dcut ，便于后续扩展

        :return: The service_group of this ShowTaskRequest.
        :rtype: str
        """
        return self._service_group

    @service_group.setter
    def service_group(self, service_group):
        r"""Sets the service_group of this ShowTaskRequest.

        服务类别，针对不同服务类场景，为用户提前填充对应值，用户侧不需单独赋值；当前仅支持 二维切割 2dcut ，便于后续扩展

        :param service_group: The service_group of this ShowTaskRequest.
        :type service_group: str
        """
        self._service_group = service_group

    @property
    def service_type(self):
        r"""Gets the service_type of this ShowTaskRequest.

        子服务类型，针对不同服务，为用户提前填充对应值，用户侧不需单独赋值；服装切割固定为 irregular-textile，雕刻机切割固定为 engraving-machine-cutting， 板材切割固定为 regular-plate

        :return: The service_type of this ShowTaskRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ShowTaskRequest.

        子服务类型，针对不同服务，为用户提前填充对应值，用户侧不需单独赋值；服装切割固定为 irregular-textile，雕刻机切割固定为 engraving-machine-cutting， 板材切割固定为 regular-plate

        :param service_type: The service_type of this ShowTaskRequest.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowTaskRequest.

        任务id

        :return: The task_id of this ShowTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowTaskRequest.

        任务id

        :param task_id: The task_id of this ShowTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def input_enable(self):
        r"""Gets the input_enable of this ShowTaskRequest.

        是否返回输入信息，默认为false； 当前暂不支持该功能，后续扩展

        :return: The input_enable of this ShowTaskRequest.
        :rtype: bool
        """
        return self._input_enable

    @input_enable.setter
    def input_enable(self, input_enable):
        r"""Sets the input_enable of this ShowTaskRequest.

        是否返回输入信息，默认为false； 当前暂不支持该功能，后续扩展

        :param input_enable: The input_enable of this ShowTaskRequest.
        :type input_enable: bool
        """
        self._input_enable = input_enable

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
        if not isinstance(other, ShowTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
