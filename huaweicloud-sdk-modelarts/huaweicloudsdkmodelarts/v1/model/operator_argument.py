# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperatorArgument:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'name': 'str',
        'type': 'OperatorArgTypeEnum',
        'tips': 'str',
        'min': 'float',
        'max': 'float',
        'between': 'bool',
        'items': 'list[OperatorArgItem]',
        'default_value': 'str',
        'required': 'bool',
        'visible': 'bool',
        'arg_display_type': 'str',
        'task_category': 'list[str]',
        'dataset_catalog': 'list[str]',
        'asset_types': 'str',
        'asset_codes': 'str',
        'sub_asset_type': 'str',
        'depend_args': 'list[DependArg]'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'type': 'type',
        'tips': 'tips',
        'min': 'min',
        'max': 'max',
        'between': 'between',
        'items': 'items',
        'default_value': 'default_value',
        'required': 'required',
        'visible': 'visible',
        'arg_display_type': 'arg_display_type',
        'task_category': 'task_category',
        'dataset_catalog': 'dataset_catalog',
        'asset_types': 'asset_types',
        'asset_codes': 'asset_codes',
        'sub_asset_type': 'sub_asset_type',
        'depend_args': 'depend_args'
    }

    def __init__(self, key=None, name=None, type=None, tips=None, min=None, max=None, between=None, items=None, default_value=None, required=None, visible=None, arg_display_type=None, task_category=None, dataset_catalog=None, asset_types=None, asset_codes=None, sub_asset_type=None, depend_args=None):
        r"""OperatorArgument

        The model defined in huaweicloud sdk

        :param key: **参数解释**：参数键
        :type key: str
        :param name: **参数解释**：参数名称
        :type name: str
        :param type: 
        :type type: :class:`huaweicloudsdkmodelarts.v1.OperatorArgTypeEnum`
        :param tips: **参数解释**：参数说明
        :type tips: str
        :param min: **参数解释**：参数最小值，数值型参数必填
        :type min: float
        :param max: **参数解释**：参数最大值，数值型参数必填
        :type max: float
        :param between: **参数解释**：是否为区间型数值
        :type between: bool
        :param items: **参数解释**：参数选项列表
        :type items: list[:class:`huaweicloudsdkmodelarts.v1.OperatorArgItem`]
        :param default_value: **参数解释**：参数默认值，用户不可见且必填的参数必须提供默认值
        :type default_value: str
        :param required: **参数解释**：参数是否必填，默认false
        :type required: bool
        :param visible: **参数解释**：该参数界面是否展示给用户配置，默认true
        :type visible: bool
        :param arg_display_type: **参数解释**：参数前端组件类型
        :type arg_display_type: str
        :param task_category: **参数解释**：数据集支持的任务类型，type为dataset时可用
        :type task_category: list[str]
        :param dataset_catalog: **参数解释**：数据集来源，type为dataset时可用
        :type dataset_catalog: list[str]
        :param asset_types: **参数解释**：资产类型,type为large_model时可用,多个以&#39;,&#39;分隔
        :type asset_types: str
        :param asset_codes: **参数解释**：资产代码,type为large_model时可用,多个以&#39;,&#39;分隔
        :type asset_codes: str
        :param sub_asset_type: **参数解释**：模型的子资产类型,type为large_model时可用
        :type sub_asset_type: str
        :param depend_args: **参数解释**：当前参数所依赖的其他参数信息列表
        :type depend_args: list[:class:`huaweicloudsdkmodelarts.v1.DependArg`]
        """
        
        

        self._key = None
        self._name = None
        self._type = None
        self._tips = None
        self._min = None
        self._max = None
        self._between = None
        self._items = None
        self._default_value = None
        self._required = None
        self._visible = None
        self._arg_display_type = None
        self._task_category = None
        self._dataset_catalog = None
        self._asset_types = None
        self._asset_codes = None
        self._sub_asset_type = None
        self._depend_args = None
        self.discriminator = None

        self.key = key
        self.name = name
        self.type = type
        if tips is not None:
            self.tips = tips
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if between is not None:
            self.between = between
        if items is not None:
            self.items = items
        if default_value is not None:
            self.default_value = default_value
        if required is not None:
            self.required = required
        if visible is not None:
            self.visible = visible
        if arg_display_type is not None:
            self.arg_display_type = arg_display_type
        if task_category is not None:
            self.task_category = task_category
        if dataset_catalog is not None:
            self.dataset_catalog = dataset_catalog
        if asset_types is not None:
            self.asset_types = asset_types
        if asset_codes is not None:
            self.asset_codes = asset_codes
        if sub_asset_type is not None:
            self.sub_asset_type = sub_asset_type
        if depend_args is not None:
            self.depend_args = depend_args

    @property
    def key(self):
        r"""Gets the key of this OperatorArgument.

        **参数解释**：参数键

        :return: The key of this OperatorArgument.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this OperatorArgument.

        **参数解释**：参数键

        :param key: The key of this OperatorArgument.
        :type key: str
        """
        self._key = key

    @property
    def name(self):
        r"""Gets the name of this OperatorArgument.

        **参数解释**：参数名称

        :return: The name of this OperatorArgument.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OperatorArgument.

        **参数解释**：参数名称

        :param name: The name of this OperatorArgument.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this OperatorArgument.

        :return: The type of this OperatorArgument.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.OperatorArgTypeEnum`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OperatorArgument.

        :param type: The type of this OperatorArgument.
        :type type: :class:`huaweicloudsdkmodelarts.v1.OperatorArgTypeEnum`
        """
        self._type = type

    @property
    def tips(self):
        r"""Gets the tips of this OperatorArgument.

        **参数解释**：参数说明

        :return: The tips of this OperatorArgument.
        :rtype: str
        """
        return self._tips

    @tips.setter
    def tips(self, tips):
        r"""Sets the tips of this OperatorArgument.

        **参数解释**：参数说明

        :param tips: The tips of this OperatorArgument.
        :type tips: str
        """
        self._tips = tips

    @property
    def min(self):
        r"""Gets the min of this OperatorArgument.

        **参数解释**：参数最小值，数值型参数必填

        :return: The min of this OperatorArgument.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this OperatorArgument.

        **参数解释**：参数最小值，数值型参数必填

        :param min: The min of this OperatorArgument.
        :type min: float
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this OperatorArgument.

        **参数解释**：参数最大值，数值型参数必填

        :return: The max of this OperatorArgument.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this OperatorArgument.

        **参数解释**：参数最大值，数值型参数必填

        :param max: The max of this OperatorArgument.
        :type max: float
        """
        self._max = max

    @property
    def between(self):
        r"""Gets the between of this OperatorArgument.

        **参数解释**：是否为区间型数值

        :return: The between of this OperatorArgument.
        :rtype: bool
        """
        return self._between

    @between.setter
    def between(self, between):
        r"""Sets the between of this OperatorArgument.

        **参数解释**：是否为区间型数值

        :param between: The between of this OperatorArgument.
        :type between: bool
        """
        self._between = between

    @property
    def items(self):
        r"""Gets the items of this OperatorArgument.

        **参数解释**：参数选项列表

        :return: The items of this OperatorArgument.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.OperatorArgItem`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this OperatorArgument.

        **参数解释**：参数选项列表

        :param items: The items of this OperatorArgument.
        :type items: list[:class:`huaweicloudsdkmodelarts.v1.OperatorArgItem`]
        """
        self._items = items

    @property
    def default_value(self):
        r"""Gets the default_value of this OperatorArgument.

        **参数解释**：参数默认值，用户不可见且必填的参数必须提供默认值

        :return: The default_value of this OperatorArgument.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this OperatorArgument.

        **参数解释**：参数默认值，用户不可见且必填的参数必须提供默认值

        :param default_value: The default_value of this OperatorArgument.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def required(self):
        r"""Gets the required of this OperatorArgument.

        **参数解释**：参数是否必填，默认false

        :return: The required of this OperatorArgument.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this OperatorArgument.

        **参数解释**：参数是否必填，默认false

        :param required: The required of this OperatorArgument.
        :type required: bool
        """
        self._required = required

    @property
    def visible(self):
        r"""Gets the visible of this OperatorArgument.

        **参数解释**：该参数界面是否展示给用户配置，默认true

        :return: The visible of this OperatorArgument.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        r"""Sets the visible of this OperatorArgument.

        **参数解释**：该参数界面是否展示给用户配置，默认true

        :param visible: The visible of this OperatorArgument.
        :type visible: bool
        """
        self._visible = visible

    @property
    def arg_display_type(self):
        r"""Gets the arg_display_type of this OperatorArgument.

        **参数解释**：参数前端组件类型

        :return: The arg_display_type of this OperatorArgument.
        :rtype: str
        """
        return self._arg_display_type

    @arg_display_type.setter
    def arg_display_type(self, arg_display_type):
        r"""Sets the arg_display_type of this OperatorArgument.

        **参数解释**：参数前端组件类型

        :param arg_display_type: The arg_display_type of this OperatorArgument.
        :type arg_display_type: str
        """
        self._arg_display_type = arg_display_type

    @property
    def task_category(self):
        r"""Gets the task_category of this OperatorArgument.

        **参数解释**：数据集支持的任务类型，type为dataset时可用

        :return: The task_category of this OperatorArgument.
        :rtype: list[str]
        """
        return self._task_category

    @task_category.setter
    def task_category(self, task_category):
        r"""Sets the task_category of this OperatorArgument.

        **参数解释**：数据集支持的任务类型，type为dataset时可用

        :param task_category: The task_category of this OperatorArgument.
        :type task_category: list[str]
        """
        self._task_category = task_category

    @property
    def dataset_catalog(self):
        r"""Gets the dataset_catalog of this OperatorArgument.

        **参数解释**：数据集来源，type为dataset时可用

        :return: The dataset_catalog of this OperatorArgument.
        :rtype: list[str]
        """
        return self._dataset_catalog

    @dataset_catalog.setter
    def dataset_catalog(self, dataset_catalog):
        r"""Sets the dataset_catalog of this OperatorArgument.

        **参数解释**：数据集来源，type为dataset时可用

        :param dataset_catalog: The dataset_catalog of this OperatorArgument.
        :type dataset_catalog: list[str]
        """
        self._dataset_catalog = dataset_catalog

    @property
    def asset_types(self):
        r"""Gets the asset_types of this OperatorArgument.

        **参数解释**：资产类型,type为large_model时可用,多个以','分隔

        :return: The asset_types of this OperatorArgument.
        :rtype: str
        """
        return self._asset_types

    @asset_types.setter
    def asset_types(self, asset_types):
        r"""Sets the asset_types of this OperatorArgument.

        **参数解释**：资产类型,type为large_model时可用,多个以','分隔

        :param asset_types: The asset_types of this OperatorArgument.
        :type asset_types: str
        """
        self._asset_types = asset_types

    @property
    def asset_codes(self):
        r"""Gets the asset_codes of this OperatorArgument.

        **参数解释**：资产代码,type为large_model时可用,多个以','分隔

        :return: The asset_codes of this OperatorArgument.
        :rtype: str
        """
        return self._asset_codes

    @asset_codes.setter
    def asset_codes(self, asset_codes):
        r"""Sets the asset_codes of this OperatorArgument.

        **参数解释**：资产代码,type为large_model时可用,多个以','分隔

        :param asset_codes: The asset_codes of this OperatorArgument.
        :type asset_codes: str
        """
        self._asset_codes = asset_codes

    @property
    def sub_asset_type(self):
        r"""Gets the sub_asset_type of this OperatorArgument.

        **参数解释**：模型的子资产类型,type为large_model时可用

        :return: The sub_asset_type of this OperatorArgument.
        :rtype: str
        """
        return self._sub_asset_type

    @sub_asset_type.setter
    def sub_asset_type(self, sub_asset_type):
        r"""Sets the sub_asset_type of this OperatorArgument.

        **参数解释**：模型的子资产类型,type为large_model时可用

        :param sub_asset_type: The sub_asset_type of this OperatorArgument.
        :type sub_asset_type: str
        """
        self._sub_asset_type = sub_asset_type

    @property
    def depend_args(self):
        r"""Gets the depend_args of this OperatorArgument.

        **参数解释**：当前参数所依赖的其他参数信息列表

        :return: The depend_args of this OperatorArgument.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.DependArg`]
        """
        return self._depend_args

    @depend_args.setter
    def depend_args(self, depend_args):
        r"""Sets the depend_args of this OperatorArgument.

        **参数解释**：当前参数所依赖的其他参数信息列表

        :param depend_args: The depend_args of this OperatorArgument.
        :type depend_args: list[:class:`huaweicloudsdkmodelarts.v1.DependArg`]
        """
        self._depend_args = depend_args

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OperatorArgument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
