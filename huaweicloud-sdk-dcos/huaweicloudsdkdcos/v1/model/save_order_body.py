# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SaveOrderBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'number': 'str',
        'title': 'str',
        'model_code': 'str',
        'access_whitelist': 'AccessWhiteList',
        'delivery_info': 'DeliveryInfo',
        'operation_objects': 'list[OperationObject]',
        'operation_attachments': 'list[UploadFileInfo]',
        'additional_attachments': 'list[UploadFileInfo]',
        'additional_content': 'str',
        'country_code': 'str',
        'phone': 'str',
        'fields': 'list[FieldEntity]',
        'is_accept_terms': 'bool'
    }

    attribute_map = {
        'number': 'number',
        'title': 'title',
        'model_code': 'model_code',
        'access_whitelist': 'access_whitelist',
        'delivery_info': 'delivery_info',
        'operation_objects': 'operation_objects',
        'operation_attachments': 'operation_attachments',
        'additional_attachments': 'additional_attachments',
        'additional_content': 'additional_content',
        'country_code': 'country_code',
        'phone': 'phone',
        'fields': 'fields',
        'is_accept_terms': 'is_accept_terms'
    }

    def __init__(self, number=None, title=None, model_code=None, access_whitelist=None, delivery_info=None, operation_objects=None, operation_attachments=None, additional_attachments=None, additional_content=None, country_code=None, phone=None, fields=None, is_accept_terms=None):
        r"""SaveOrderBody

        The model defined in huaweicloud sdk

        :param number: 服务单号，修改已保存的草稿时使用
        :type number: str
        :param title: 标题
        :type title: str
        :param model_code: 服务单类型编码
        :type model_code: str
        :param access_whitelist: 
        :type access_whitelist: :class:`huaweicloudsdkdcos.v1.AccessWhiteList`
        :param delivery_info: 
        :type delivery_info: :class:`huaweicloudsdkdcos.v1.DeliveryInfo`
        :param operation_objects: 操作对象
        :type operation_objects: list[:class:`huaweicloudsdkdcos.v1.OperationObject`]
        :param operation_attachments: 操作内容附件
        :type operation_attachments: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        :param additional_attachments: 补充附件
        :type additional_attachments: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        :param additional_content: 补充说明
        :type additional_content: str
        :param country_code: 手机国际码
        :type country_code: str
        :param phone: 联系电话
        :type phone: str
        :param fields: 扩展字段
        :type fields: list[:class:`huaweicloudsdkdcos.v1.FieldEntity`]
        :param is_accept_terms: 是否同意服务条款
        :type is_accept_terms: bool
        """
        
        

        self._number = None
        self._title = None
        self._model_code = None
        self._access_whitelist = None
        self._delivery_info = None
        self._operation_objects = None
        self._operation_attachments = None
        self._additional_attachments = None
        self._additional_content = None
        self._country_code = None
        self._phone = None
        self._fields = None
        self._is_accept_terms = None
        self.discriminator = None

        if number is not None:
            self.number = number
        self.title = title
        self.model_code = model_code
        if access_whitelist is not None:
            self.access_whitelist = access_whitelist
        if delivery_info is not None:
            self.delivery_info = delivery_info
        if operation_objects is not None:
            self.operation_objects = operation_objects
        if operation_attachments is not None:
            self.operation_attachments = operation_attachments
        if additional_attachments is not None:
            self.additional_attachments = additional_attachments
        if additional_content is not None:
            self.additional_content = additional_content
        if country_code is not None:
            self.country_code = country_code
        if phone is not None:
            self.phone = phone
        if fields is not None:
            self.fields = fields
        self.is_accept_terms = is_accept_terms

    @property
    def number(self):
        r"""Gets the number of this SaveOrderBody.

        服务单号，修改已保存的草稿时使用

        :return: The number of this SaveOrderBody.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this SaveOrderBody.

        服务单号，修改已保存的草稿时使用

        :param number: The number of this SaveOrderBody.
        :type number: str
        """
        self._number = number

    @property
    def title(self):
        r"""Gets the title of this SaveOrderBody.

        标题

        :return: The title of this SaveOrderBody.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this SaveOrderBody.

        标题

        :param title: The title of this SaveOrderBody.
        :type title: str
        """
        self._title = title

    @property
    def model_code(self):
        r"""Gets the model_code of this SaveOrderBody.

        服务单类型编码

        :return: The model_code of this SaveOrderBody.
        :rtype: str
        """
        return self._model_code

    @model_code.setter
    def model_code(self, model_code):
        r"""Sets the model_code of this SaveOrderBody.

        服务单类型编码

        :param model_code: The model_code of this SaveOrderBody.
        :type model_code: str
        """
        self._model_code = model_code

    @property
    def access_whitelist(self):
        r"""Gets the access_whitelist of this SaveOrderBody.

        :return: The access_whitelist of this SaveOrderBody.
        :rtype: :class:`huaweicloudsdkdcos.v1.AccessWhiteList`
        """
        return self._access_whitelist

    @access_whitelist.setter
    def access_whitelist(self, access_whitelist):
        r"""Sets the access_whitelist of this SaveOrderBody.

        :param access_whitelist: The access_whitelist of this SaveOrderBody.
        :type access_whitelist: :class:`huaweicloudsdkdcos.v1.AccessWhiteList`
        """
        self._access_whitelist = access_whitelist

    @property
    def delivery_info(self):
        r"""Gets the delivery_info of this SaveOrderBody.

        :return: The delivery_info of this SaveOrderBody.
        :rtype: :class:`huaweicloudsdkdcos.v1.DeliveryInfo`
        """
        return self._delivery_info

    @delivery_info.setter
    def delivery_info(self, delivery_info):
        r"""Sets the delivery_info of this SaveOrderBody.

        :param delivery_info: The delivery_info of this SaveOrderBody.
        :type delivery_info: :class:`huaweicloudsdkdcos.v1.DeliveryInfo`
        """
        self._delivery_info = delivery_info

    @property
    def operation_objects(self):
        r"""Gets the operation_objects of this SaveOrderBody.

        操作对象

        :return: The operation_objects of this SaveOrderBody.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.OperationObject`]
        """
        return self._operation_objects

    @operation_objects.setter
    def operation_objects(self, operation_objects):
        r"""Sets the operation_objects of this SaveOrderBody.

        操作对象

        :param operation_objects: The operation_objects of this SaveOrderBody.
        :type operation_objects: list[:class:`huaweicloudsdkdcos.v1.OperationObject`]
        """
        self._operation_objects = operation_objects

    @property
    def operation_attachments(self):
        r"""Gets the operation_attachments of this SaveOrderBody.

        操作内容附件

        :return: The operation_attachments of this SaveOrderBody.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        """
        return self._operation_attachments

    @operation_attachments.setter
    def operation_attachments(self, operation_attachments):
        r"""Sets the operation_attachments of this SaveOrderBody.

        操作内容附件

        :param operation_attachments: The operation_attachments of this SaveOrderBody.
        :type operation_attachments: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        """
        self._operation_attachments = operation_attachments

    @property
    def additional_attachments(self):
        r"""Gets the additional_attachments of this SaveOrderBody.

        补充附件

        :return: The additional_attachments of this SaveOrderBody.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        """
        return self._additional_attachments

    @additional_attachments.setter
    def additional_attachments(self, additional_attachments):
        r"""Sets the additional_attachments of this SaveOrderBody.

        补充附件

        :param additional_attachments: The additional_attachments of this SaveOrderBody.
        :type additional_attachments: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        """
        self._additional_attachments = additional_attachments

    @property
    def additional_content(self):
        r"""Gets the additional_content of this SaveOrderBody.

        补充说明

        :return: The additional_content of this SaveOrderBody.
        :rtype: str
        """
        return self._additional_content

    @additional_content.setter
    def additional_content(self, additional_content):
        r"""Sets the additional_content of this SaveOrderBody.

        补充说明

        :param additional_content: The additional_content of this SaveOrderBody.
        :type additional_content: str
        """
        self._additional_content = additional_content

    @property
    def country_code(self):
        r"""Gets the country_code of this SaveOrderBody.

        手机国际码

        :return: The country_code of this SaveOrderBody.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        r"""Sets the country_code of this SaveOrderBody.

        手机国际码

        :param country_code: The country_code of this SaveOrderBody.
        :type country_code: str
        """
        self._country_code = country_code

    @property
    def phone(self):
        r"""Gets the phone of this SaveOrderBody.

        联系电话

        :return: The phone of this SaveOrderBody.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this SaveOrderBody.

        联系电话

        :param phone: The phone of this SaveOrderBody.
        :type phone: str
        """
        self._phone = phone

    @property
    def fields(self):
        r"""Gets the fields of this SaveOrderBody.

        扩展字段

        :return: The fields of this SaveOrderBody.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.FieldEntity`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this SaveOrderBody.

        扩展字段

        :param fields: The fields of this SaveOrderBody.
        :type fields: list[:class:`huaweicloudsdkdcos.v1.FieldEntity`]
        """
        self._fields = fields

    @property
    def is_accept_terms(self):
        r"""Gets the is_accept_terms of this SaveOrderBody.

        是否同意服务条款

        :return: The is_accept_terms of this SaveOrderBody.
        :rtype: bool
        """
        return self._is_accept_terms

    @is_accept_terms.setter
    def is_accept_terms(self, is_accept_terms):
        r"""Sets the is_accept_terms of this SaveOrderBody.

        是否同意服务条款

        :param is_accept_terms: The is_accept_terms of this SaveOrderBody.
        :type is_accept_terms: bool
        """
        self._is_accept_terms = is_accept_terms

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
        if not isinstance(other, SaveOrderBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
