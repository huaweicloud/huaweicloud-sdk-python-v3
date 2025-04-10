# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FgacSingleUpdateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dw_id': 'str',
        'fgac_flag': 'bool',
        'fgac_type': 'str'
    }

    attribute_map = {
        'dw_id': 'dw_id',
        'fgac_flag': 'fgac_flag',
        'fgac_type': 'fgac_type'
    }

    def __init__(self, dw_id=None, fgac_flag=None, fgac_type=None):
        r"""FgacSingleUpdateReq

        The model defined in huaweicloud sdk

        :param dw_id: 数据连接id
        :type dw_id: str
        :param fgac_flag: 是否开启细粒度认证,true表示开启细粒度认证,false表示关闭细粒度认证。
        :type fgac_flag: bool
        :param fgac_type: 细粒度认证类型，开启细粒度认证时才生效。\&quot;0\&quot;表示开发态细粒度认证，支持数据开发细粒度脚本运行、作业测试运行，\&quot;1\&quot;表示调度态细粒度认证，支持数据开发细粒度脚本运行、作业测试运行、作业执行调度。
        :type fgac_type: str
        """
        
        

        self._dw_id = None
        self._fgac_flag = None
        self._fgac_type = None
        self.discriminator = None

        if dw_id is not None:
            self.dw_id = dw_id
        if fgac_flag is not None:
            self.fgac_flag = fgac_flag
        if fgac_type is not None:
            self.fgac_type = fgac_type

    @property
    def dw_id(self):
        r"""Gets the dw_id of this FgacSingleUpdateReq.

        数据连接id

        :return: The dw_id of this FgacSingleUpdateReq.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        r"""Sets the dw_id of this FgacSingleUpdateReq.

        数据连接id

        :param dw_id: The dw_id of this FgacSingleUpdateReq.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def fgac_flag(self):
        r"""Gets the fgac_flag of this FgacSingleUpdateReq.

        是否开启细粒度认证,true表示开启细粒度认证,false表示关闭细粒度认证。

        :return: The fgac_flag of this FgacSingleUpdateReq.
        :rtype: bool
        """
        return self._fgac_flag

    @fgac_flag.setter
    def fgac_flag(self, fgac_flag):
        r"""Sets the fgac_flag of this FgacSingleUpdateReq.

        是否开启细粒度认证,true表示开启细粒度认证,false表示关闭细粒度认证。

        :param fgac_flag: The fgac_flag of this FgacSingleUpdateReq.
        :type fgac_flag: bool
        """
        self._fgac_flag = fgac_flag

    @property
    def fgac_type(self):
        r"""Gets the fgac_type of this FgacSingleUpdateReq.

        细粒度认证类型，开启细粒度认证时才生效。\"0\"表示开发态细粒度认证，支持数据开发细粒度脚本运行、作业测试运行，\"1\"表示调度态细粒度认证，支持数据开发细粒度脚本运行、作业测试运行、作业执行调度。

        :return: The fgac_type of this FgacSingleUpdateReq.
        :rtype: str
        """
        return self._fgac_type

    @fgac_type.setter
    def fgac_type(self, fgac_type):
        r"""Sets the fgac_type of this FgacSingleUpdateReq.

        细粒度认证类型，开启细粒度认证时才生效。\"0\"表示开发态细粒度认证，支持数据开发细粒度脚本运行、作业测试运行，\"1\"表示调度态细粒度认证，支持数据开发细粒度脚本运行、作业测试运行、作业执行调度。

        :param fgac_type: The fgac_type of this FgacSingleUpdateReq.
        :type fgac_type: str
        """
        self._fgac_type = fgac_type

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
        if not isinstance(other, FgacSingleUpdateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
