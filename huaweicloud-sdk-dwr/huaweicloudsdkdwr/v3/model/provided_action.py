# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProvidedAction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_name': 'str',
        'category': 'str',
        'create_time': 'str',
        'last_modify_time': 'str',
        'inputs': 'list[Input]',
        'dynamic_source_definition': 'dict(str, object)',
        'need_policy': 'list[Policy]',
        'provider_name': 'str',
        'is_uploaded_func_pkg': 'bool',
        'func_pkg_endpoint': 'str',
        'upload_func_pkg_size': 'int',
        'upload_func_pkg_etag': 'str',
        'register_status': 'PublicTemplateRegisterType',
        'description': 'str',
        'function_template': 'str',
        'provider_domainid': 'str',
        'provider_userid': 'str'
    }

    attribute_map = {
        'template_name': 'template_name',
        'category': 'category',
        'create_time': 'create_time',
        'last_modify_time': 'last_modify_time',
        'inputs': 'inputs',
        'dynamic_source_definition': 'dynamic_source_definition',
        'need_policy': 'need_policy',
        'provider_name': 'provider_name',
        'is_uploaded_func_pkg': 'is_uploaded_func_pkg',
        'func_pkg_endpoint': 'func_pkg_endpoint',
        'upload_func_pkg_size': 'upload_func_pkg_size',
        'upload_func_pkg_etag': 'upload_func_pkg_etag',
        'register_status': 'register_status',
        'description': 'description',
        'function_template': 'function_template',
        'provider_domainid': 'provider_domainid',
        'provider_userid': 'provider_userid'
    }

    def __init__(self, template_name=None, category=None, create_time=None, last_modify_time=None, inputs=None, dynamic_source_definition=None, need_policy=None, provider_name=None, is_uploaded_func_pkg=None, func_pkg_endpoint=None, upload_func_pkg_size=None, upload_func_pkg_etag=None, register_status=None, description=None, function_template=None, provider_domainid=None, provider_userid=None):
        """ProvidedAction

        The model defined in huaweicloud sdk

        :param template_name: 算子模板名称。
        :type template_name: str
        :param category: 分类。默认分类为FileProcess,MediaProcess,ImageProcess,ContentReview,NotificationProcess,VoiceInteraction
        :type category: str
        :param create_time: 创建时间。
        :type create_time: str
        :param last_modify_time: 最近修改时间。
        :type last_modify_time: str
        :param inputs: 可修改参数定义列表。
        :type inputs: list[:class:`huaweicloudsdkdwr.v3.Input`]
        :param dynamic_source_definition: 可修改参数引用
        :type dynamic_source_definition: dict(str, object)
        :param need_policy: 需要的权限。
        :type need_policy: list[:class:`huaweicloudsdkdwr.v3.Policy`]
        :param provider_name: 算子提供方名称。
        :type provider_name: str
        :param is_uploaded_func_pkg: 是否上传了算子包
        :type is_uploaded_func_pkg: bool
        :param func_pkg_endpoint: 上传算子包的临时签名URL地址，用于上传算子包。
        :type func_pkg_endpoint: str
        :param upload_func_pkg_size: 上传算子包的大小。小于100M
        :type upload_func_pkg_size: int
        :param upload_func_pkg_etag: 上传算子包的etag。
        :type upload_func_pkg_etag: str
        :param register_status: 
        :type register_status: :class:`huaweicloudsdkdwr.v3.PublicTemplateRegisterType`
        :param description: 描述。
        :type description: str
        :param function_template: 函数URN
        :type function_template: str
        :param provider_domainid: 算子提供方IAM DomainID
        :type provider_domainid: str
        :param provider_userid: 算子提供方IAM UserID
        :type provider_userid: str
        """
        
        

        self._template_name = None
        self._category = None
        self._create_time = None
        self._last_modify_time = None
        self._inputs = None
        self._dynamic_source_definition = None
        self._need_policy = None
        self._provider_name = None
        self._is_uploaded_func_pkg = None
        self._func_pkg_endpoint = None
        self._upload_func_pkg_size = None
        self._upload_func_pkg_etag = None
        self._register_status = None
        self._description = None
        self._function_template = None
        self._provider_domainid = None
        self._provider_userid = None
        self.discriminator = None

        self.template_name = template_name
        self.category = category
        self.create_time = create_time
        if last_modify_time is not None:
            self.last_modify_time = last_modify_time
        if inputs is not None:
            self.inputs = inputs
        self.dynamic_source_definition = dynamic_source_definition
        self.need_policy = need_policy
        self.provider_name = provider_name
        self.is_uploaded_func_pkg = is_uploaded_func_pkg
        self.func_pkg_endpoint = func_pkg_endpoint
        if upload_func_pkg_size is not None:
            self.upload_func_pkg_size = upload_func_pkg_size
        if upload_func_pkg_etag is not None:
            self.upload_func_pkg_etag = upload_func_pkg_etag
        self.register_status = register_status
        if description is not None:
            self.description = description
        self.function_template = function_template
        self.provider_domainid = provider_domainid
        if provider_userid is not None:
            self.provider_userid = provider_userid

    @property
    def template_name(self):
        """Gets the template_name of this ProvidedAction.

        算子模板名称。

        :return: The template_name of this ProvidedAction.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this ProvidedAction.

        算子模板名称。

        :param template_name: The template_name of this ProvidedAction.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def category(self):
        """Gets the category of this ProvidedAction.

        分类。默认分类为FileProcess,MediaProcess,ImageProcess,ContentReview,NotificationProcess,VoiceInteraction

        :return: The category of this ProvidedAction.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ProvidedAction.

        分类。默认分类为FileProcess,MediaProcess,ImageProcess,ContentReview,NotificationProcess,VoiceInteraction

        :param category: The category of this ProvidedAction.
        :type category: str
        """
        self._category = category

    @property
    def create_time(self):
        """Gets the create_time of this ProvidedAction.

        创建时间。

        :return: The create_time of this ProvidedAction.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ProvidedAction.

        创建时间。

        :param create_time: The create_time of this ProvidedAction.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_modify_time(self):
        """Gets the last_modify_time of this ProvidedAction.

        最近修改时间。

        :return: The last_modify_time of this ProvidedAction.
        :rtype: str
        """
        return self._last_modify_time

    @last_modify_time.setter
    def last_modify_time(self, last_modify_time):
        """Sets the last_modify_time of this ProvidedAction.

        最近修改时间。

        :param last_modify_time: The last_modify_time of this ProvidedAction.
        :type last_modify_time: str
        """
        self._last_modify_time = last_modify_time

    @property
    def inputs(self):
        """Gets the inputs of this ProvidedAction.

        可修改参数定义列表。

        :return: The inputs of this ProvidedAction.
        :rtype: list[:class:`huaweicloudsdkdwr.v3.Input`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this ProvidedAction.

        可修改参数定义列表。

        :param inputs: The inputs of this ProvidedAction.
        :type inputs: list[:class:`huaweicloudsdkdwr.v3.Input`]
        """
        self._inputs = inputs

    @property
    def dynamic_source_definition(self):
        """Gets the dynamic_source_definition of this ProvidedAction.

        可修改参数引用

        :return: The dynamic_source_definition of this ProvidedAction.
        :rtype: dict(str, object)
        """
        return self._dynamic_source_definition

    @dynamic_source_definition.setter
    def dynamic_source_definition(self, dynamic_source_definition):
        """Sets the dynamic_source_definition of this ProvidedAction.

        可修改参数引用

        :param dynamic_source_definition: The dynamic_source_definition of this ProvidedAction.
        :type dynamic_source_definition: dict(str, object)
        """
        self._dynamic_source_definition = dynamic_source_definition

    @property
    def need_policy(self):
        """Gets the need_policy of this ProvidedAction.

        需要的权限。

        :return: The need_policy of this ProvidedAction.
        :rtype: list[:class:`huaweicloudsdkdwr.v3.Policy`]
        """
        return self._need_policy

    @need_policy.setter
    def need_policy(self, need_policy):
        """Sets the need_policy of this ProvidedAction.

        需要的权限。

        :param need_policy: The need_policy of this ProvidedAction.
        :type need_policy: list[:class:`huaweicloudsdkdwr.v3.Policy`]
        """
        self._need_policy = need_policy

    @property
    def provider_name(self):
        """Gets the provider_name of this ProvidedAction.

        算子提供方名称。

        :return: The provider_name of this ProvidedAction.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this ProvidedAction.

        算子提供方名称。

        :param provider_name: The provider_name of this ProvidedAction.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def is_uploaded_func_pkg(self):
        """Gets the is_uploaded_func_pkg of this ProvidedAction.

        是否上传了算子包

        :return: The is_uploaded_func_pkg of this ProvidedAction.
        :rtype: bool
        """
        return self._is_uploaded_func_pkg

    @is_uploaded_func_pkg.setter
    def is_uploaded_func_pkg(self, is_uploaded_func_pkg):
        """Sets the is_uploaded_func_pkg of this ProvidedAction.

        是否上传了算子包

        :param is_uploaded_func_pkg: The is_uploaded_func_pkg of this ProvidedAction.
        :type is_uploaded_func_pkg: bool
        """
        self._is_uploaded_func_pkg = is_uploaded_func_pkg

    @property
    def func_pkg_endpoint(self):
        """Gets the func_pkg_endpoint of this ProvidedAction.

        上传算子包的临时签名URL地址，用于上传算子包。

        :return: The func_pkg_endpoint of this ProvidedAction.
        :rtype: str
        """
        return self._func_pkg_endpoint

    @func_pkg_endpoint.setter
    def func_pkg_endpoint(self, func_pkg_endpoint):
        """Sets the func_pkg_endpoint of this ProvidedAction.

        上传算子包的临时签名URL地址，用于上传算子包。

        :param func_pkg_endpoint: The func_pkg_endpoint of this ProvidedAction.
        :type func_pkg_endpoint: str
        """
        self._func_pkg_endpoint = func_pkg_endpoint

    @property
    def upload_func_pkg_size(self):
        """Gets the upload_func_pkg_size of this ProvidedAction.

        上传算子包的大小。小于100M

        :return: The upload_func_pkg_size of this ProvidedAction.
        :rtype: int
        """
        return self._upload_func_pkg_size

    @upload_func_pkg_size.setter
    def upload_func_pkg_size(self, upload_func_pkg_size):
        """Sets the upload_func_pkg_size of this ProvidedAction.

        上传算子包的大小。小于100M

        :param upload_func_pkg_size: The upload_func_pkg_size of this ProvidedAction.
        :type upload_func_pkg_size: int
        """
        self._upload_func_pkg_size = upload_func_pkg_size

    @property
    def upload_func_pkg_etag(self):
        """Gets the upload_func_pkg_etag of this ProvidedAction.

        上传算子包的etag。

        :return: The upload_func_pkg_etag of this ProvidedAction.
        :rtype: str
        """
        return self._upload_func_pkg_etag

    @upload_func_pkg_etag.setter
    def upload_func_pkg_etag(self, upload_func_pkg_etag):
        """Sets the upload_func_pkg_etag of this ProvidedAction.

        上传算子包的etag。

        :param upload_func_pkg_etag: The upload_func_pkg_etag of this ProvidedAction.
        :type upload_func_pkg_etag: str
        """
        self._upload_func_pkg_etag = upload_func_pkg_etag

    @property
    def register_status(self):
        """Gets the register_status of this ProvidedAction.

        :return: The register_status of this ProvidedAction.
        :rtype: :class:`huaweicloudsdkdwr.v3.PublicTemplateRegisterType`
        """
        return self._register_status

    @register_status.setter
    def register_status(self, register_status):
        """Sets the register_status of this ProvidedAction.

        :param register_status: The register_status of this ProvidedAction.
        :type register_status: :class:`huaweicloudsdkdwr.v3.PublicTemplateRegisterType`
        """
        self._register_status = register_status

    @property
    def description(self):
        """Gets the description of this ProvidedAction.

        描述。

        :return: The description of this ProvidedAction.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProvidedAction.

        描述。

        :param description: The description of this ProvidedAction.
        :type description: str
        """
        self._description = description

    @property
    def function_template(self):
        """Gets the function_template of this ProvidedAction.

        函数URN

        :return: The function_template of this ProvidedAction.
        :rtype: str
        """
        return self._function_template

    @function_template.setter
    def function_template(self, function_template):
        """Sets the function_template of this ProvidedAction.

        函数URN

        :param function_template: The function_template of this ProvidedAction.
        :type function_template: str
        """
        self._function_template = function_template

    @property
    def provider_domainid(self):
        """Gets the provider_domainid of this ProvidedAction.

        算子提供方IAM DomainID

        :return: The provider_domainid of this ProvidedAction.
        :rtype: str
        """
        return self._provider_domainid

    @provider_domainid.setter
    def provider_domainid(self, provider_domainid):
        """Sets the provider_domainid of this ProvidedAction.

        算子提供方IAM DomainID

        :param provider_domainid: The provider_domainid of this ProvidedAction.
        :type provider_domainid: str
        """
        self._provider_domainid = provider_domainid

    @property
    def provider_userid(self):
        """Gets the provider_userid of this ProvidedAction.

        算子提供方IAM UserID

        :return: The provider_userid of this ProvidedAction.
        :rtype: str
        """
        return self._provider_userid

    @provider_userid.setter
    def provider_userid(self, provider_userid):
        """Sets the provider_userid of this ProvidedAction.

        算子提供方IAM UserID

        :param provider_userid: The provider_userid of this ProvidedAction.
        :type provider_userid: str
        """
        self._provider_userid = provider_userid

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
        if not isinstance(other, ProvidedAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
