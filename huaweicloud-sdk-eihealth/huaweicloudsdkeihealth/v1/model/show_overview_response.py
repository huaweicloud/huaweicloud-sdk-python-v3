# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOverviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'storage': 'int',
        'project_num': 'int',
        'charge_mode': 'int'
    }

    attribute_map = {
        'id': 'id',
        'storage': 'storage',
        'project_num': 'project_num',
        'charge_mode': 'charge_mode'
    }

    def __init__(self, id=None, storage=None, project_num=None, charge_mode=None):
        """ShowOverviewResponse

        The model defined in huaweicloud sdk

        :param id: 平台ID
        :type id: str
        :param storage: 存储量，单位：byte
        :type storage: int
        :param project_num: 项目总数
        :type project_num: int
        :param charge_mode: 计费模式
        :type charge_mode: int
        """
        
        super(ShowOverviewResponse, self).__init__()

        self._id = None
        self._storage = None
        self._project_num = None
        self._charge_mode = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if storage is not None:
            self.storage = storage
        if project_num is not None:
            self.project_num = project_num
        if charge_mode is not None:
            self.charge_mode = charge_mode

    @property
    def id(self):
        """Gets the id of this ShowOverviewResponse.

        平台ID

        :return: The id of this ShowOverviewResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowOverviewResponse.

        平台ID

        :param id: The id of this ShowOverviewResponse.
        :type id: str
        """
        self._id = id

    @property
    def storage(self):
        """Gets the storage of this ShowOverviewResponse.

        存储量，单位：byte

        :return: The storage of this ShowOverviewResponse.
        :rtype: int
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this ShowOverviewResponse.

        存储量，单位：byte

        :param storage: The storage of this ShowOverviewResponse.
        :type storage: int
        """
        self._storage = storage

    @property
    def project_num(self):
        """Gets the project_num of this ShowOverviewResponse.

        项目总数

        :return: The project_num of this ShowOverviewResponse.
        :rtype: int
        """
        return self._project_num

    @project_num.setter
    def project_num(self, project_num):
        """Sets the project_num of this ShowOverviewResponse.

        项目总数

        :param project_num: The project_num of this ShowOverviewResponse.
        :type project_num: int
        """
        self._project_num = project_num

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ShowOverviewResponse.

        计费模式

        :return: The charge_mode of this ShowOverviewResponse.
        :rtype: int
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ShowOverviewResponse.

        计费模式

        :param charge_mode: The charge_mode of this ShowOverviewResponse.
        :type charge_mode: int
        """
        self._charge_mode = charge_mode

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
        if not isinstance(other, ShowOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
