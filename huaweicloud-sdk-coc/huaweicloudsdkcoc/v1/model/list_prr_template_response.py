# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPrrTemplateResponse(SdkResponse):

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
        'name': 'str',
        'application_type': 'str',
        'description': 'str',
        'creator': 'str',
        'creator_name': 'str',
        'create_time': 'int',
        'last_update_time': 'int',
        'is_related_review': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'application_type': 'application_type',
        'description': 'description',
        'creator': 'creator',
        'creator_name': 'creator_name',
        'create_time': 'create_time',
        'last_update_time': 'last_update_time',
        'is_related_review': 'is_related_review'
    }

    def __init__(self, id=None, name=None, application_type=None, description=None, creator=None, creator_name=None, create_time=None, last_update_time=None, is_related_review=None):
        """ListPrrTemplateResponse

        The model defined in huaweicloud sdk

        :param id: PRR模板id
        :type id: str
        :param name: 模板名称
        :type name: str
        :param application_type: 应用分类
        :type application_type: str
        :param description: 模板描述
        :type description: str
        :param creator: 创建人id
        :type creator: str
        :param creator_name: 创建人名称
        :type creator_name: str
        :param create_time: 创建时间
        :type create_time: int
        :param last_update_time: 最后更新时间
        :type last_update_time: int
        :param is_related_review: 是否已关联检查项
        :type is_related_review: bool
        """
        
        super(ListPrrTemplateResponse, self).__init__()

        self._id = None
        self._name = None
        self._application_type = None
        self._description = None
        self._creator = None
        self._creator_name = None
        self._create_time = None
        self._last_update_time = None
        self._is_related_review = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if application_type is not None:
            self.application_type = application_type
        if description is not None:
            self.description = description
        if creator is not None:
            self.creator = creator
        if creator_name is not None:
            self.creator_name = creator_name
        if create_time is not None:
            self.create_time = create_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if is_related_review is not None:
            self.is_related_review = is_related_review

    @property
    def id(self):
        """Gets the id of this ListPrrTemplateResponse.

        PRR模板id

        :return: The id of this ListPrrTemplateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListPrrTemplateResponse.

        PRR模板id

        :param id: The id of this ListPrrTemplateResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListPrrTemplateResponse.

        模板名称

        :return: The name of this ListPrrTemplateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPrrTemplateResponse.

        模板名称

        :param name: The name of this ListPrrTemplateResponse.
        :type name: str
        """
        self._name = name

    @property
    def application_type(self):
        """Gets the application_type of this ListPrrTemplateResponse.

        应用分类

        :return: The application_type of this ListPrrTemplateResponse.
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """Sets the application_type of this ListPrrTemplateResponse.

        应用分类

        :param application_type: The application_type of this ListPrrTemplateResponse.
        :type application_type: str
        """
        self._application_type = application_type

    @property
    def description(self):
        """Gets the description of this ListPrrTemplateResponse.

        模板描述

        :return: The description of this ListPrrTemplateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListPrrTemplateResponse.

        模板描述

        :param description: The description of this ListPrrTemplateResponse.
        :type description: str
        """
        self._description = description

    @property
    def creator(self):
        """Gets the creator of this ListPrrTemplateResponse.

        创建人id

        :return: The creator of this ListPrrTemplateResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ListPrrTemplateResponse.

        创建人id

        :param creator: The creator of this ListPrrTemplateResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def creator_name(self):
        """Gets the creator_name of this ListPrrTemplateResponse.

        创建人名称

        :return: The creator_name of this ListPrrTemplateResponse.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this ListPrrTemplateResponse.

        创建人名称

        :param creator_name: The creator_name of this ListPrrTemplateResponse.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def create_time(self):
        """Gets the create_time of this ListPrrTemplateResponse.

        创建时间

        :return: The create_time of this ListPrrTemplateResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ListPrrTemplateResponse.

        创建时间

        :param create_time: The create_time of this ListPrrTemplateResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def last_update_time(self):
        """Gets the last_update_time of this ListPrrTemplateResponse.

        最后更新时间

        :return: The last_update_time of this ListPrrTemplateResponse.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this ListPrrTemplateResponse.

        最后更新时间

        :param last_update_time: The last_update_time of this ListPrrTemplateResponse.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

    @property
    def is_related_review(self):
        """Gets the is_related_review of this ListPrrTemplateResponse.

        是否已关联检查项

        :return: The is_related_review of this ListPrrTemplateResponse.
        :rtype: bool
        """
        return self._is_related_review

    @is_related_review.setter
    def is_related_review(self, is_related_review):
        """Sets the is_related_review of this ListPrrTemplateResponse.

        是否已关联检查项

        :param is_related_review: The is_related_review of this ListPrrTemplateResponse.
        :type is_related_review: bool
        """
        self._is_related_review = is_related_review

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
        if not isinstance(other, ListPrrTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
