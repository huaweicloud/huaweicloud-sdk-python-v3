# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplayCompareResultResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_template': 'str',
        'sql_template_md5': 'str',
        'sql_params': 'str',
        'target_content': 'str',
        'mirror_content': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'sql_template': 'sql_template',
        'sql_template_md5': 'sql_template_md5',
        'sql_params': 'sql_params',
        'target_content': 'target_content',
        'mirror_content': 'mirror_content',
        'create_time': 'create_time'
    }

    def __init__(self, sql_template=None, sql_template_md5=None, sql_params=None, target_content=None, mirror_content=None, create_time=None):
        r"""ReplayCompareResultResp

        The model defined in huaweicloud sdk

        :param sql_template: SQL模板
        :type sql_template: str
        :param sql_template_md5: SQL模板MD5哈希值
        :type sql_template_md5: str
        :param sql_params: SQL参数
        :type sql_params: str
        :param target_content: 目标库内容
        :type target_content: str
        :param mirror_content: 镜像库内容
        :type mirror_content: str
        :param create_time: 创建时间
        :type create_time: str
        """
        
        

        self._sql_template = None
        self._sql_template_md5 = None
        self._sql_params = None
        self._target_content = None
        self._mirror_content = None
        self._create_time = None
        self.discriminator = None

        if sql_template is not None:
            self.sql_template = sql_template
        if sql_template_md5 is not None:
            self.sql_template_md5 = sql_template_md5
        if sql_params is not None:
            self.sql_params = sql_params
        if target_content is not None:
            self.target_content = target_content
        if mirror_content is not None:
            self.mirror_content = mirror_content
        if create_time is not None:
            self.create_time = create_time

    @property
    def sql_template(self):
        r"""Gets the sql_template of this ReplayCompareResultResp.

        SQL模板

        :return: The sql_template of this ReplayCompareResultResp.
        :rtype: str
        """
        return self._sql_template

    @sql_template.setter
    def sql_template(self, sql_template):
        r"""Sets the sql_template of this ReplayCompareResultResp.

        SQL模板

        :param sql_template: The sql_template of this ReplayCompareResultResp.
        :type sql_template: str
        """
        self._sql_template = sql_template

    @property
    def sql_template_md5(self):
        r"""Gets the sql_template_md5 of this ReplayCompareResultResp.

        SQL模板MD5哈希值

        :return: The sql_template_md5 of this ReplayCompareResultResp.
        :rtype: str
        """
        return self._sql_template_md5

    @sql_template_md5.setter
    def sql_template_md5(self, sql_template_md5):
        r"""Sets the sql_template_md5 of this ReplayCompareResultResp.

        SQL模板MD5哈希值

        :param sql_template_md5: The sql_template_md5 of this ReplayCompareResultResp.
        :type sql_template_md5: str
        """
        self._sql_template_md5 = sql_template_md5

    @property
    def sql_params(self):
        r"""Gets the sql_params of this ReplayCompareResultResp.

        SQL参数

        :return: The sql_params of this ReplayCompareResultResp.
        :rtype: str
        """
        return self._sql_params

    @sql_params.setter
    def sql_params(self, sql_params):
        r"""Sets the sql_params of this ReplayCompareResultResp.

        SQL参数

        :param sql_params: The sql_params of this ReplayCompareResultResp.
        :type sql_params: str
        """
        self._sql_params = sql_params

    @property
    def target_content(self):
        r"""Gets the target_content of this ReplayCompareResultResp.

        目标库内容

        :return: The target_content of this ReplayCompareResultResp.
        :rtype: str
        """
        return self._target_content

    @target_content.setter
    def target_content(self, target_content):
        r"""Sets the target_content of this ReplayCompareResultResp.

        目标库内容

        :param target_content: The target_content of this ReplayCompareResultResp.
        :type target_content: str
        """
        self._target_content = target_content

    @property
    def mirror_content(self):
        r"""Gets the mirror_content of this ReplayCompareResultResp.

        镜像库内容

        :return: The mirror_content of this ReplayCompareResultResp.
        :rtype: str
        """
        return self._mirror_content

    @mirror_content.setter
    def mirror_content(self, mirror_content):
        r"""Sets the mirror_content of this ReplayCompareResultResp.

        镜像库内容

        :param mirror_content: The mirror_content of this ReplayCompareResultResp.
        :type mirror_content: str
        """
        self._mirror_content = mirror_content

    @property
    def create_time(self):
        r"""Gets the create_time of this ReplayCompareResultResp.

        创建时间

        :return: The create_time of this ReplayCompareResultResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ReplayCompareResultResp.

        创建时间

        :param create_time: The create_time of this ReplayCompareResultResp.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, ReplayCompareResultResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
