# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudPhonesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'phone_name': 'str',
        'server_id': 'str',
        'status': 'int',
        'type': 'int'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'phone_name': 'phone_name',
        'server_id': 'server_id',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, offset=None, limit=None, phone_name=None, server_id=None, status=None, type=None):
        """ListCloudPhonesRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源数，默认值为0。
        :type offset: int
        :param limit: 每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。
        :type limit: int
        :param phone_name: 云手机名称，支持模糊查询
        :type phone_name: str
        :param server_id: 服务器id。
        :type server_id: str
        :param status: 云手机状态 - 0：创建中 - 1：创建中 - 2：运行中 - 3：重置中 - 4：重启中 - 6：冻结 - 7：正在关机 - 8：已关机 - -5：重置失败 - -6：重启失败 - -7：手机异常 - -8：创建失败 - -9：关机失败
        :type status: int
        :param type: 云手机类型 - 0：普通云手机 - 1：试玩云手机
        :type type: int
        """
        
        

        self._offset = None
        self._limit = None
        self._phone_name = None
        self._server_id = None
        self._status = None
        self._type = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if phone_name is not None:
            self.phone_name = phone_name
        if server_id is not None:
            self.server_id = server_id
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def offset(self):
        """Gets the offset of this ListCloudPhonesRequest.

        偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源数，默认值为0。

        :return: The offset of this ListCloudPhonesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCloudPhonesRequest.

        偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源数，默认值为0。

        :param offset: The offset of this ListCloudPhonesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListCloudPhonesRequest.

        每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :return: The limit of this ListCloudPhonesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCloudPhonesRequest.

        每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :param limit: The limit of this ListCloudPhonesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def phone_name(self):
        """Gets the phone_name of this ListCloudPhonesRequest.

        云手机名称，支持模糊查询

        :return: The phone_name of this ListCloudPhonesRequest.
        :rtype: str
        """
        return self._phone_name

    @phone_name.setter
    def phone_name(self, phone_name):
        """Sets the phone_name of this ListCloudPhonesRequest.

        云手机名称，支持模糊查询

        :param phone_name: The phone_name of this ListCloudPhonesRequest.
        :type phone_name: str
        """
        self._phone_name = phone_name

    @property
    def server_id(self):
        """Gets the server_id of this ListCloudPhonesRequest.

        服务器id。

        :return: The server_id of this ListCloudPhonesRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ListCloudPhonesRequest.

        服务器id。

        :param server_id: The server_id of this ListCloudPhonesRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def status(self):
        """Gets the status of this ListCloudPhonesRequest.

        云手机状态 - 0：创建中 - 1：创建中 - 2：运行中 - 3：重置中 - 4：重启中 - 6：冻结 - 7：正在关机 - 8：已关机 - -5：重置失败 - -6：重启失败 - -7：手机异常 - -8：创建失败 - -9：关机失败

        :return: The status of this ListCloudPhonesRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListCloudPhonesRequest.

        云手机状态 - 0：创建中 - 1：创建中 - 2：运行中 - 3：重置中 - 4：重启中 - 6：冻结 - 7：正在关机 - 8：已关机 - -5：重置失败 - -6：重启失败 - -7：手机异常 - -8：创建失败 - -9：关机失败

        :param status: The status of this ListCloudPhonesRequest.
        :type status: int
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ListCloudPhonesRequest.

        云手机类型 - 0：普通云手机 - 1：试玩云手机

        :return: The type of this ListCloudPhonesRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListCloudPhonesRequest.

        云手机类型 - 0：普通云手机 - 1：试玩云手机

        :param type: The type of this ListCloudPhonesRequest.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, ListCloudPhonesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
