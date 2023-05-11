# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Regular:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'l2_regularization': 'float',
        'regular_loss_compute_mode': 'str',
        'embed_l2_regularization': 'float',
        'wide_l2_regularization': 'float',
        'structure_l2_regularization': 'float'
    }

    attribute_map = {
        'l2_regularization': 'l2_regularization',
        'regular_loss_compute_mode': 'regular_loss_compute_mode',
        'embed_l2_regularization': 'embed_l2_regularization',
        'wide_l2_regularization': 'wide_l2_regularization',
        'structure_l2_regularization': 'structure_l2_regularization'
    }

    def __init__(self, l2_regularization=None, regular_loss_compute_mode=None, embed_l2_regularization=None, wide_l2_regularization=None, structure_l2_regularization=None):
        """Regular

        The model defined in huaweicloud sdk

        :param l2_regularization: L2正则项系数。
        :type l2_regularization: float
        :param regular_loss_compute_mode: 正则损失计算方式。
        :type regular_loss_compute_mode: str
        :param embed_l2_regularization: 隐向量层L2正则化系数。
        :type embed_l2_regularization: float
        :param wide_l2_regularization: wide部分L2正则化系数。
        :type wide_l2_regularization: float
        :param structure_l2_regularization: 结构化部分L2正则化系数。
        :type structure_l2_regularization: float
        """
        
        

        self._l2_regularization = None
        self._regular_loss_compute_mode = None
        self._embed_l2_regularization = None
        self._wide_l2_regularization = None
        self._structure_l2_regularization = None
        self.discriminator = None

        if l2_regularization is not None:
            self.l2_regularization = l2_regularization
        if regular_loss_compute_mode is not None:
            self.regular_loss_compute_mode = regular_loss_compute_mode
        if embed_l2_regularization is not None:
            self.embed_l2_regularization = embed_l2_regularization
        if wide_l2_regularization is not None:
            self.wide_l2_regularization = wide_l2_regularization
        if structure_l2_regularization is not None:
            self.structure_l2_regularization = structure_l2_regularization

    @property
    def l2_regularization(self):
        """Gets the l2_regularization of this Regular.

        L2正则项系数。

        :return: The l2_regularization of this Regular.
        :rtype: float
        """
        return self._l2_regularization

    @l2_regularization.setter
    def l2_regularization(self, l2_regularization):
        """Sets the l2_regularization of this Regular.

        L2正则项系数。

        :param l2_regularization: The l2_regularization of this Regular.
        :type l2_regularization: float
        """
        self._l2_regularization = l2_regularization

    @property
    def regular_loss_compute_mode(self):
        """Gets the regular_loss_compute_mode of this Regular.

        正则损失计算方式。

        :return: The regular_loss_compute_mode of this Regular.
        :rtype: str
        """
        return self._regular_loss_compute_mode

    @regular_loss_compute_mode.setter
    def regular_loss_compute_mode(self, regular_loss_compute_mode):
        """Sets the regular_loss_compute_mode of this Regular.

        正则损失计算方式。

        :param regular_loss_compute_mode: The regular_loss_compute_mode of this Regular.
        :type regular_loss_compute_mode: str
        """
        self._regular_loss_compute_mode = regular_loss_compute_mode

    @property
    def embed_l2_regularization(self):
        """Gets the embed_l2_regularization of this Regular.

        隐向量层L2正则化系数。

        :return: The embed_l2_regularization of this Regular.
        :rtype: float
        """
        return self._embed_l2_regularization

    @embed_l2_regularization.setter
    def embed_l2_regularization(self, embed_l2_regularization):
        """Sets the embed_l2_regularization of this Regular.

        隐向量层L2正则化系数。

        :param embed_l2_regularization: The embed_l2_regularization of this Regular.
        :type embed_l2_regularization: float
        """
        self._embed_l2_regularization = embed_l2_regularization

    @property
    def wide_l2_regularization(self):
        """Gets the wide_l2_regularization of this Regular.

        wide部分L2正则化系数。

        :return: The wide_l2_regularization of this Regular.
        :rtype: float
        """
        return self._wide_l2_regularization

    @wide_l2_regularization.setter
    def wide_l2_regularization(self, wide_l2_regularization):
        """Sets the wide_l2_regularization of this Regular.

        wide部分L2正则化系数。

        :param wide_l2_regularization: The wide_l2_regularization of this Regular.
        :type wide_l2_regularization: float
        """
        self._wide_l2_regularization = wide_l2_regularization

    @property
    def structure_l2_regularization(self):
        """Gets the structure_l2_regularization of this Regular.

        结构化部分L2正则化系数。

        :return: The structure_l2_regularization of this Regular.
        :rtype: float
        """
        return self._structure_l2_regularization

    @structure_l2_regularization.setter
    def structure_l2_regularization(self, structure_l2_regularization):
        """Sets the structure_l2_regularization of this Regular.

        结构化部分L2正则化系数。

        :param structure_l2_regularization: The structure_l2_regularization of this Regular.
        :type structure_l2_regularization: float
        """
        self._structure_l2_regularization = structure_l2_regularization

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
        if not isinstance(other, Regular):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
