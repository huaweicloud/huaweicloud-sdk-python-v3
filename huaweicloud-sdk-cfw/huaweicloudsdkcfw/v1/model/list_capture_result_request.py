# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCaptureResultRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fw_instance_id': 'str',
        'task_id': 'str',
        'type': 'int',
        'ip': 'list[str]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'task_id': 'task_id',
        'type': 'type',
        'ip': 'ip',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, fw_instance_id=None, task_id=None, type=None, ip=None, enterprise_project_id=None):
        r"""ListCaptureResultRequest

        The model defined in huaweicloud sdk

        :param fw_instance_id: 防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        :param task_id: 抓包任务id，可通过[查询抓包任务接口](ListCaptureTask.xml)查询获得，通过返回值中的data.records.task_id（.表示各对象之间层级的区分）获得。
        :type task_id: str
        :param type: 是否指定公网ip下载，0：无限制，1：指定公网ip下载
        :type type: int
        :param ip: 指定公网ip
        :type ip: list[str]
        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        """
        
        

        self._fw_instance_id = None
        self._task_id = None
        self._type = None
        self._ip = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.fw_instance_id = fw_instance_id
        self.task_id = task_id
        if type is not None:
            self.type = type
        if ip is not None:
            self.ip = ip
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ListCaptureResultRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this ListCaptureResultRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ListCaptureResultRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this ListCaptureResultRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ListCaptureResultRequest.

        抓包任务id，可通过[查询抓包任务接口](ListCaptureTask.xml)查询获得，通过返回值中的data.records.task_id（.表示各对象之间层级的区分）获得。

        :return: The task_id of this ListCaptureResultRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListCaptureResultRequest.

        抓包任务id，可通过[查询抓包任务接口](ListCaptureTask.xml)查询获得，通过返回值中的data.records.task_id（.表示各对象之间层级的区分）获得。

        :param task_id: The task_id of this ListCaptureResultRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def type(self):
        r"""Gets the type of this ListCaptureResultRequest.

        是否指定公网ip下载，0：无限制，1：指定公网ip下载

        :return: The type of this ListCaptureResultRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListCaptureResultRequest.

        是否指定公网ip下载，0：无限制，1：指定公网ip下载

        :param type: The type of this ListCaptureResultRequest.
        :type type: int
        """
        self._type = type

    @property
    def ip(self):
        r"""Gets the ip of this ListCaptureResultRequest.

        指定公网ip

        :return: The ip of this ListCaptureResultRequest.
        :rtype: list[str]
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ListCaptureResultRequest.

        指定公网ip

        :param ip: The ip of this ListCaptureResultRequest.
        :type ip: list[str]
        """
        self._ip = ip

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListCaptureResultRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this ListCaptureResultRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListCaptureResultRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this ListCaptureResultRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListCaptureResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
