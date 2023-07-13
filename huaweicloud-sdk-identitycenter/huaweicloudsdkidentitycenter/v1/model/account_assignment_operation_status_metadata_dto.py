# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccountAssignmentOperationStatusMetadataDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_date': 'int',
        'request_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'created_date': 'created_date',
        'request_id': 'request_id',
        'status': 'status'
    }

    def __init__(self, created_date=None, request_id=None, status=None):
        """AccountAssignmentOperationStatusMetadataDto

        The model defined in huaweicloud sdk

        :param created_date: 创建日期
        :type created_date: int
        :param request_id: 请求唯一标识
        :type request_id: str
        :param status: 权限集授权状态
        :type status: str
        """
        
        

        self._created_date = None
        self._request_id = None
        self._status = None
        self.discriminator = None

        if created_date is not None:
            self.created_date = created_date
        if request_id is not None:
            self.request_id = request_id
        if status is not None:
            self.status = status

    @property
    def created_date(self):
        """Gets the created_date of this AccountAssignmentOperationStatusMetadataDto.

        创建日期

        :return: The created_date of this AccountAssignmentOperationStatusMetadataDto.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this AccountAssignmentOperationStatusMetadataDto.

        创建日期

        :param created_date: The created_date of this AccountAssignmentOperationStatusMetadataDto.
        :type created_date: int
        """
        self._created_date = created_date

    @property
    def request_id(self):
        """Gets the request_id of this AccountAssignmentOperationStatusMetadataDto.

        请求唯一标识

        :return: The request_id of this AccountAssignmentOperationStatusMetadataDto.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this AccountAssignmentOperationStatusMetadataDto.

        请求唯一标识

        :param request_id: The request_id of this AccountAssignmentOperationStatusMetadataDto.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def status(self):
        """Gets the status of this AccountAssignmentOperationStatusMetadataDto.

        权限集授权状态

        :return: The status of this AccountAssignmentOperationStatusMetadataDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountAssignmentOperationStatusMetadataDto.

        权限集授权状态

        :param status: The status of this AccountAssignmentOperationStatusMetadataDto.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, AccountAssignmentOperationStatusMetadataDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
