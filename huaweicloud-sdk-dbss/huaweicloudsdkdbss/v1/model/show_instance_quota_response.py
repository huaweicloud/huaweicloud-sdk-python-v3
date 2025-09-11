# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceQuotaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu': 'int',
        'project_id': 'str',
        'quota': 'int',
        'ram': 'int'
    }

    attribute_map = {
        'cpu': 'cpu',
        'project_id': 'project_id',
        'quota': 'quota',
        'ram': 'ram'
    }

    def __init__(self, cpu=None, project_id=None, quota=None, ram=None):
        r"""ShowInstanceQuotaResponse

        The model defined in huaweicloud sdk

        :param cpu: CPU个数
        :type cpu: int
        :param project_id: 项目ID
        :type project_id: str
        :param quota: 实例配额
        :type quota: int
        :param ram: 内存大小MB
        :type ram: int
        """
        
        super(ShowInstanceQuotaResponse, self).__init__()

        self._cpu = None
        self._project_id = None
        self._quota = None
        self._ram = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if project_id is not None:
            self.project_id = project_id
        if quota is not None:
            self.quota = quota
        if ram is not None:
            self.ram = ram

    @property
    def cpu(self):
        r"""Gets the cpu of this ShowInstanceQuotaResponse.

        CPU个数

        :return: The cpu of this ShowInstanceQuotaResponse.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ShowInstanceQuotaResponse.

        CPU个数

        :param cpu: The cpu of this ShowInstanceQuotaResponse.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowInstanceQuotaResponse.

        项目ID

        :return: The project_id of this ShowInstanceQuotaResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowInstanceQuotaResponse.

        项目ID

        :param project_id: The project_id of this ShowInstanceQuotaResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def quota(self):
        r"""Gets the quota of this ShowInstanceQuotaResponse.

        实例配额

        :return: The quota of this ShowInstanceQuotaResponse.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this ShowInstanceQuotaResponse.

        实例配额

        :param quota: The quota of this ShowInstanceQuotaResponse.
        :type quota: int
        """
        self._quota = quota

    @property
    def ram(self):
        r"""Gets the ram of this ShowInstanceQuotaResponse.

        内存大小MB

        :return: The ram of this ShowInstanceQuotaResponse.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this ShowInstanceQuotaResponse.

        内存大小MB

        :param ram: The ram of this ShowInstanceQuotaResponse.
        :type ram: int
        """
        self._ram = ram

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
        if not isinstance(other, ShowInstanceQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
