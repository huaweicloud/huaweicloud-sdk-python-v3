# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProductTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'status': 'int',
        'created_user': 'CreatedUser',
        'last_updated_user': 'LastUpdatedUser',
        'created_datetime': 'int',
        'last_updated_datetime': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'created_user': 'created_user',
        'last_updated_user': 'last_updated_user',
        'created_datetime': 'created_datetime',
        'last_updated_datetime': 'last_updated_datetime'
    }

    def __init__(self, id=None, name=None, description=None, status=None, created_user=None, last_updated_user=None, created_datetime=None, last_updated_datetime=None):
        r"""CreateProductTemplateResponse

        The model defined in huaweicloud sdk

        :param id: 产品模板ID
        :type id: int
        :param name: 产品模板名称
        :type name: str
        :param description: 产品模板描述
        :type description: str
        :param status: 产品模板状态 0-启用 1-停用
        :type status: int
        :param created_user: 
        :type created_user: :class:`huaweicloudsdkroma.v2.CreatedUser`
        :param last_updated_user: 
        :type last_updated_user: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        :param created_datetime: 创建时间，timestamp(ms)，使用UTC时区
        :type created_datetime: int
        :param last_updated_datetime: 最后修改时间，timestamp(ms)，使用UTC时区
        :type last_updated_datetime: int
        """
        
        super(CreateProductTemplateResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._created_user = None
        self._last_updated_user = None
        self._created_datetime = None
        self._last_updated_datetime = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if created_user is not None:
            self.created_user = created_user
        if last_updated_user is not None:
            self.last_updated_user = last_updated_user
        if created_datetime is not None:
            self.created_datetime = created_datetime
        if last_updated_datetime is not None:
            self.last_updated_datetime = last_updated_datetime

    @property
    def id(self):
        r"""Gets the id of this CreateProductTemplateResponse.

        产品模板ID

        :return: The id of this CreateProductTemplateResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateProductTemplateResponse.

        产品模板ID

        :param id: The id of this CreateProductTemplateResponse.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateProductTemplateResponse.

        产品模板名称

        :return: The name of this CreateProductTemplateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateProductTemplateResponse.

        产品模板名称

        :param name: The name of this CreateProductTemplateResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateProductTemplateResponse.

        产品模板描述

        :return: The description of this CreateProductTemplateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateProductTemplateResponse.

        产品模板描述

        :param description: The description of this CreateProductTemplateResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this CreateProductTemplateResponse.

        产品模板状态 0-启用 1-停用

        :return: The status of this CreateProductTemplateResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateProductTemplateResponse.

        产品模板状态 0-启用 1-停用

        :param status: The status of this CreateProductTemplateResponse.
        :type status: int
        """
        self._status = status

    @property
    def created_user(self):
        r"""Gets the created_user of this CreateProductTemplateResponse.

        :return: The created_user of this CreateProductTemplateResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.CreatedUser`
        """
        return self._created_user

    @created_user.setter
    def created_user(self, created_user):
        r"""Sets the created_user of this CreateProductTemplateResponse.

        :param created_user: The created_user of this CreateProductTemplateResponse.
        :type created_user: :class:`huaweicloudsdkroma.v2.CreatedUser`
        """
        self._created_user = created_user

    @property
    def last_updated_user(self):
        r"""Gets the last_updated_user of this CreateProductTemplateResponse.

        :return: The last_updated_user of this CreateProductTemplateResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        """
        return self._last_updated_user

    @last_updated_user.setter
    def last_updated_user(self, last_updated_user):
        r"""Sets the last_updated_user of this CreateProductTemplateResponse.

        :param last_updated_user: The last_updated_user of this CreateProductTemplateResponse.
        :type last_updated_user: :class:`huaweicloudsdkroma.v2.LastUpdatedUser`
        """
        self._last_updated_user = last_updated_user

    @property
    def created_datetime(self):
        r"""Gets the created_datetime of this CreateProductTemplateResponse.

        创建时间，timestamp(ms)，使用UTC时区

        :return: The created_datetime of this CreateProductTemplateResponse.
        :rtype: int
        """
        return self._created_datetime

    @created_datetime.setter
    def created_datetime(self, created_datetime):
        r"""Sets the created_datetime of this CreateProductTemplateResponse.

        创建时间，timestamp(ms)，使用UTC时区

        :param created_datetime: The created_datetime of this CreateProductTemplateResponse.
        :type created_datetime: int
        """
        self._created_datetime = created_datetime

    @property
    def last_updated_datetime(self):
        r"""Gets the last_updated_datetime of this CreateProductTemplateResponse.

        最后修改时间，timestamp(ms)，使用UTC时区

        :return: The last_updated_datetime of this CreateProductTemplateResponse.
        :rtype: int
        """
        return self._last_updated_datetime

    @last_updated_datetime.setter
    def last_updated_datetime(self, last_updated_datetime):
        r"""Sets the last_updated_datetime of this CreateProductTemplateResponse.

        最后修改时间，timestamp(ms)，使用UTC时区

        :param last_updated_datetime: The last_updated_datetime of this CreateProductTemplateResponse.
        :type last_updated_datetime: int
        """
        self._last_updated_datetime = last_updated_datetime

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
        if not isinstance(other, CreateProductTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
